document.addEventListener("DOMContentLoaded", () => {
  const collectionList = document.getElementById("collection-list");
  const collectionDetail = document.getElementById("collection-detail");
  let allCollections = [];
  function loadData() {
    fetch("get_collections_data/")
      .then((response) => response.json())
      .then((data) => {
        let collectionData = data.collections;
        // console.log(collectionData);
        displayCollections(collectionData);
      })
      .catch((error) => {
        console.error(
          "Une erreur est survenue lors de la récupération des données",
          error
        );
      });
  }
  if (collectionList !== null) {
    loadData();
  }

  function displayCollections(list) {
    collectionList.innerHTML = "";
    const collections = list;

    collections.forEach((collection) => {
      const collectionDiv = document.createElement("div");
      const collectionObjects = document.createElement("ul");
      const collectionTitle = document.createElement("h2");
      collectionTitle.textContent = collection.name;
      collectionTitle.style.cursor = "pointer";
      collectionTitle.addEventListener("click", () => {
        const collectionId = collection.id;
        const collectionDetailsUrl = new URL(
          `/collection/collection_details/?id=${collectionId}`,
          window.location.origin
        );
        window.location.href = collectionDetailsUrl.href;
      });
      collectionDiv.appendChild(collectionTitle);
      // collectionDiv.innerHTML = `
      //   <h2>${collection.name}</h2>`;
      collection.collection_object.forEach((object) => {
        const objectItem = document.createElement("li");
        objectItem.textContent = object.object_name;
        // console.log(object.object_name);
        collectionObjects.appendChild(objectItem);

        // console.log(collectionObjects);
      });
      collectionDiv.appendChild(collectionObjects);
      collectionList.appendChild(collectionDiv);
    });
  }
  function loadCollectionDetails(collectionId) {
    if (collectionId) {
      fetch(`/collection/get_collection_details/${collectionId}/`)
        .then((response) => response.json())
        .then((data) => {
          // console.log(data);
          updateCollectionDetail(data);
        })
        .catch((error) => {
          console.error("Une erreur est survenue : ", error);
        });
    }
  }
  function updateCollectionDetail(data) {
    const collectionName = document.getElementById("collection-name");
    const collectionCategory = document.getElementById("collection-category");
    const collectionObjects = document.getElementById("collection-objects");

    collectionName.textContent = data.name;
    collectionCategory.textContent = `Catégorie: ${data.category}`;
    collectionObjects.innerHTML = "";
    data.collection_objects.forEach((object) => {
      const objectItem = document.createElement("li");
      objectItem.textContent = `${object.name} : ${object.description}`;
      if (object.image) {
        const imageElement = document.createElement("img");
        console.log(imageElement);
        console.log(object.image);

        imageElement.src = object.image;
        imageElement.alt = object.name;
        console.log(imageElement.src);
        objectItem.appendChild(imageElement);
      }
      collectionObjects.appendChild(objectItem);
    });
  }
  if (collectionDetail !== null) {
    const params = new URLSearchParams(window.location.search);
    const collectionId = params.get("id");

    loadCollectionDetails(collectionId);
  }
});
