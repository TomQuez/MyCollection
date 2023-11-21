document.addEventListener("DOMContentLoaded", () => {
  const collectionList = document.getElementById("collection-list");
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

  loadData();
  function displayCollections(list) {
    collectionList.innerHTML = "";
    const collections = list;

    collections.forEach((collection) => {
      const collectionDiv = document.createElement("div");

      collectionDiv.innerHTML = `
        <h2>${collection.name}</h2>
        
        `;
      collectionList.appendChild(collectionDiv);
    });
  }
});