document.addEventListener("DOMContentLoaded", () => {
  const menuCategory = document.querySelectorAll(".menu-category");
  const coffeeMenuCategory = document.querySelector(".coffee-menu-category");
  const coffeeCategory = document.querySelector(".coffee-category");
  const lunchMenuCategory = document.querySelector(".lunch-menu-category");
  const lunchCategory = document.querySelector(".lunch-category");
  const dinnerMenuCategory = document.querySelector(".dinner-menu-category");
  const dinnerCategory = document.querySelector(".dinner-category");
  const dessertMenuCategory = document.querySelector(".dessert-menu-category");
  const dessertCategory = document.querySelector(".dessert-category");
  const drinksMenuCategory = document.querySelector(".drinks-menu-category");
  const drinkCategory = document.querySelector(".drinks-category");

  for (let i = 0; i < menuCategory.length; i++) {
    const element = menuCategory[i];

    element.addEventListener("mouseover", function () {
      element.classList.add("hover");
    });
    element.addEventListener("mouseout", function () {
      element.classList.remove("hover");
    });

    element.addEventListener("click", function () {
      clearItems();
      const categoryId = element.getAttribute("data-category-id");
      loadMenuItems(categoryId);
    });
  }

  function loadMenuItems(categoryId) {
    fetch(`/getItems/${categoryId}/`)
      .then((response) => response.json())
      .then((data) => {
        let categoryName = data.name.toLowerCase() + "-category";
        console.log(categoryName);
        const categoryClass = document.querySelector("." + categoryName);
        categoryClass.innerHTML = ""; // Clear existing elements

        data.items.forEach((subcategory) => {
          console.log("subcategory: " + subcategory.subcategory);

          const categoryDiv = document.createElement("div");
          categoryDiv.classList.add("category-div");

          const categoryItem = document.createElement("div");
          categoryItem.classList.add("category-item");

          const subcategoryLabel = document.createElement("label");
          subcategoryLabel.textContent = subcategory.subcategory;

          const itemsDiv = document.createElement("div");
          itemsDiv.className = "items-div";

          categoryItem.appendChild(subcategoryLabel);
          categoryDiv.appendChild(categoryItem);
          categoryDiv.appendChild(itemsDiv);
          categoryClass.appendChild(categoryDiv);

          subcategory.menu_items.forEach((menuItem) => {
            console.log(menuItem.name);

            const itemDiv = document.createElement("div");
            itemDiv.className = "item";

            const itemName = document.createElement("div");
            itemName.classList.add("item-name");

            const itemNameLabel = document.createElement("label");
            itemNameLabel.textContent = menuItem.name;

            itemName.appendChild(itemNameLabel);
            itemDiv.appendChild(itemName);
            itemsDiv.appendChild(itemDiv);
          });
        });
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  function clearItems() {
    const categoryClass = document.getElementById("categoryClass");
    categoryClass.innerHTML = "";
  }

  coffeeMenuCategory.addEventListener("click", () => {
    coffeeMenuCategory.classList.add("active");
    coffeeCategory.style.display = "flex";
    lunchMenuCategory.classList.remove("active");
    lunchCategory.style.display = "none";
    dinnerMenuCategory.classList.remove("active");
    dinnerCategory.style.display = "none";
    dessertMenuCategory.classList.remove("active");
    dessertCategory.style.display = "none";
    drinksMenuCategory.classList.remove("active");
    drinkCategory.style.display = "none";
  });

  lunchMenuCategory.addEventListener("click", () => {
    coffeeMenuCategory.classList.remove("active");
    coffeeCategory.style.display = "none";
    lunchMenuCategory.classList.add("active");
    lunchCategory.style.display = "flex";
    dinnerMenuCategory.classList.remove("active");
    dinnerCategory.style.display = "none";
    dessertMenuCategory.classList.remove("active");
    dessertCategory.style.display = "none";
    drinksMenuCategory.classList.remove("active");
    drinkCategory.style.display = "none";
  });

  dinnerMenuCategory.addEventListener("click", () => {
    coffeeMenuCategory.classList.remove("active");
    coffeeCategory.style.display = "none";
    lunchMenuCategory.classList.remove("active");
    lunchCategory.style.display = "none";
    dinnerMenuCategory.classList.add("active");
    dinnerCategory.style.display = "flex";
    dessertMenuCategory.classList.remove("active");
    dessertCategory.style.display = "none";
    drinksMenuCategory.classList.remove("active");
    drinkCategory.style.display = "none";
  });

  dessertMenuCategory.addEventListener("click", () => {
    coffeeMenuCategory.classList.remove("active");
    coffeeCategory.style.display = "none";
    lunchMenuCategory.classList.remove("active");
    lunchCategory.style.display = "none";
    dinnerMenuCategory.classList.remove("active");
    dinnerCategory.style.display = "none";
    dessertMenuCategory.classList.add("active");
    dessertCategory.style.display = "flex";
    drinksMenuCategory.classList.remove("active");
    drinkCategory.style.display = "none";
  });

  drinksMenuCategory.addEventListener("click", () => {
    coffeeMenuCategory.classList.remove("active");
    coffeeCategory.style.display = "none";
    lunchMenuCategory.classList.remove("active");
    lunchCategory.style.display = "none";
    dinnerMenuCategory.classList.remove("active");
    dinnerCategory.style.display = "none";
    dessertMenuCategory.classList.remove("active");
    dessertCategory.style.display = "none";
    drinksMenuCategory.classList.add("active");
    drinkCategory.style.display = "flex";
  });

  coffeeMenuCategory.click();
});
