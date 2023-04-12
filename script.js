"use strict";

// Fetch the JSON data from the file
fetch("output.json")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Failed to fetch the JSON data.");
    }
    return response.json();
  })
  .then((outputJson) => {
    // Parse the chat history
    const chatHistory = outputJson.chat_history;

    // Select the div with the class 'story'
    const storyDiv = document.querySelector(".story");

    // Iterate through the chat history and create a paragraph element for each item
    chatHistory.forEach((item) => {
      const paragraph = document.createElement("p");
      paragraph.innerText = item.text;
      storyDiv.appendChild(paragraph);
    });
  })
  .catch((error) => {
    console.error("Error:", error);
  });

// Dom scripts
const menuBtn = document.querySelector(".menu-btn");
const menu = document.querySelector(".menu");
const menuNav = document.querySelector(".menu-nav");
const menuBranding = document.querySelector(".menu-branding");
const navItems = document.querySelectorAll(".nav-item");

let showMenu = false;

menuBtn.addEventListener("click", toggleMenu);

function toggleMenu() {
  if (!showMenu) {
    menuBtn.classList.add("close");
    menu.classList.add("show");
    menuNav.classList.add("show");
    menuBranding.classList.add("show");
    navItems.forEach((item) => item.classList.add("show"));
    showMenu = true;
  } else {
    menuBtn.classList.remove("close");
    menu.classList.remove("show");
    menuNav.classList.remove("show");
    menuBranding.classList.remove("show");
    navItems.forEach((item) => item.classList.remove("show"));
    showMenu = false;
  }
}

const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const btnCloseModal = document.querySelector(".close-modal");
const btnsOpenModal = document.querySelectorAll(".show-modal");
const bodyTag = document.querySelector("body");

const openModal = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
  bodyTag.classList.add("modal-open");
};

const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

for (let i = 0; i < btnsOpenModal.length; i++)
  btnsOpenModal[i].addEventListener("click", openModal);

btnCloseModal.addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});
