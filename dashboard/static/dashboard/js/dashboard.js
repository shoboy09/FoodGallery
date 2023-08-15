document.addEventListener("DOMContentLoaded", function () {
  function updateTime() {
    const currentTimeElement = document.querySelector(".time");
    const currentDateElement = document.querySelector(".date");
    const timeNow = new Date();
    const hours = (timeNow.getHours() % 12 || 12).toString().padStart(2, "0");
    const minutes = timeNow.getMinutes().toString().padStart(2, "0");
    const seconds = timeNow.getSeconds().toString().padStart(2, "0");
    const ampm = timeNow.getHours() >= 12 ? "PM" : "AM";
    const timeString = `${hours}:${minutes}:${seconds} ${ampm}`;
    currentTimeElement.textContent = timeString;
    const options = { year: "numeric", month: "long", day: "numeric" };
    const dateNow = new Date();
    const dateString = dateNow.toLocaleDateString("en-US", options);
    currentDateElement.textContent = dateString;
  }
  setInterval(updateTime, 1000);
  updateTime();
});
