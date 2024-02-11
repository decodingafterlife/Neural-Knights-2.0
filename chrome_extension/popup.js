import { getActiveTabURL } from "./background.js";

document.addEventListener("DOMContentLoaded", async () => {
  const urlDiv = document.getElementById("url");
  const socialMediaText = document.getElementById("socialMediaText");
  const jsonTable = document.getElementById("jsonTable");

  // Display "Loading..." text while waiting for data
  urlDiv.textContent = "Loading...";
  socialMediaText.textContent = "Loading...";
  jsonTable.innerHTML = "<tr><td colspan='2'>Loading...</td></tr>";

  try {
    const tab = await getActiveTabURL();

    // Display the URL
    urlDiv.textContent = tab.url;
    const res = await fetch(
      `http://localhost:8000/api?link=${urlDiv.textContent}`,
      { mode: "no-cors" }
    );
    // Load the JSON data from output.json
    const response = await fetch("./output.json");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();

    // Convert JSON data into a table
    let tableHtml = "<table>";
    for (const [key, value] of Object.entries(data)) {
      tableHtml += `<tr><td>${key}</td><td>${value}</td></tr>`;
    }
    tableHtml += "</table>";
    jsonTable.innerHTML = tableHtml;

    // List of social media keywords
    const socialMediaKeywords = [
      "whatsapp",
      "facebook",
      "youtube",
      "instagram",
      // Add more social media keywords as needed
    ];

    // Function to check if the URL contains social media keywords
    function isSocialMedia(url) {
      for (const keyword of socialMediaKeywords) {
        if (url.includes(keyword)) {
          return true;
        }
      }
      return false;
    }

    // Check if the URL contains social media keywords
    const isSocial = isSocialMedia(tab.url);
    if (isSocial) {
      socialMediaText.textContent = "The URL is of a social media platform.";
    } else {
      socialMediaText.textContent =
        "The URL is not of a social media platform.";
    }
  } catch (error) {
    console.error("Error fetching or parsing data:", error);
    // Display error message if there's an issue with fetching or parsing data
    urlDiv.textContent = "Error loading data";
    socialMediaText.textContent = "";
    jsonTable.innerHTML = "";
  }
});
