document.addEventListener("DOMContentLoaded", () => {
  const content = document.querySelector(".content");
  const bookingContent = document.querySelector(".booking-content");
  const bookingsDiv = document.querySelector(".bookings-div");
  let isDragging = false;
  const dragOffset = { x: 0, y: 0 };
  const originalPosition = { x: 0, y: 0 };

  // Event listener for the toggle button
  bookingsDiv.addEventListener("click", () => {
    if (bookingContent.classList.contains("hidden")) {
      bookingContent.classList.remove("hidden");
      resetPosition();
    } else {
      bookingContent.classList.add("hidden");
    }
  });

  bookingContent.addEventListener("mousedown", (event) => {
    isDragging = true;
    dragOffset.x = event.clientX - bookingContent.offsetLeft;
    dragOffset.y = event.clientY - bookingContent.offsetTop;
  });

  document.addEventListener("mousemove", (event) => {
    if (isDragging) {
      const contentRect = content.getBoundingClientRect();
      const minX = 0;
      const minY = 0;
      const maxX = contentRect.width - bookingContent.offsetWidth;
      const maxY = contentRect.height - bookingContent.offsetHeight;

      let newX = event.clientX - dragOffset.x;
      let newY = event.clientY - dragOffset.y;

      // Limit dragging within the container boundaries
      newX = Math.max(minX, Math.min(newX, maxX));
      newY = Math.max(minY, Math.min(newY, maxY));

      bookingContent.style.left = newX + "px";
      bookingContent.style.top = newY + "px";
    }
  });

  document.addEventListener("mouseup", () => {
    isDragging = false;
    originalPosition.x = bookingContent.offsetLeft;
    originalPosition.y = bookingContent.offsetTop;
  });

  // Function to reset the position of the draggable div
  const resetPosition = () => {
    bookingContent.style.left = "2%";
    bookingContent.style.top = "5%";
  };

  // Function to hide the draggable div when clicking outside
  const hideOnClickOutside = (event) => {
    if (
      !bookingContent.contains(event.target) &&
      !bookingsDiv.contains(event.target)
    ) {
      bookingContent.classList.add("hidden");
    }
  };

  // Add click event listener to document
  document.addEventListener("click", hideOnClickOutside);

  const reserveBtn = document.querySelector(".reserve-btn");
  const reservationContent = document.querySelector(".reservation-content");

  reserveBtn.addEventListener("click", () => {
    reservationContent.style.display = "flex";
  });

  document.addEventListener("click", (event) => {
    if (
      !reservationContent.contains(event.target) &&
      event.target !== reserveBtn
    ) {
      reservationContent.style.display = "none";
    }
  });

  // const reserveUserIcons = document.querySelectorAll(".reserve-user-icon");

  // reserveUserIcons.forEach((reserveUserIcon) => {
  //   reserveUserIcon.addEventListener("mouseover", () => {
  //     reserveUserIcon.classList.remove("fa-regular");
  //     reserveUserIcon.classList.add("fa-solid");
  //   });

  //   reserveUserIcon.addEventListener("mouseout", () => {
  //     reserveUserIcon.classList.remove("fa-solid");
  //     reserveUserIcon.classList.add("fa-regular");
  //   });
  // });

  // Get references to all the available table buttons
  const reserveButtons = document.querySelectorAll(
    ".available-table-reserve-btn"
  );
  const reservationTable = document.querySelector(".reservation-table");

  // Attach event listeners to each reserve button
  reserveButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      event.stopPropagation();
      const tableLabel = event.currentTarget.parentNode.querySelector("label");
      const tableNumber = tableLabel.textContent.split(" ")[1];
      const rtbLabel = document.querySelector(".rtb label");
      rtbLabel.textContent = tableNumber;
      reservationContent.style.display = "none";
      reservationTable.style.display = "flex";
    });
  });

  document.addEventListener("click", (event) => {
    const isClickedOutside = !reservationTable.contains(event.target);
    if (isClickedOutside) {
      reservationTable.style.display = "none";
    }
  });

  const updateDateTime = () => {
    const date = new Date();
    const time = date.toLocaleTimeString();
    const day = date.toLocaleDateString("en-US", { weekday: "short" });
    const formattedDate = date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    });

    document.querySelector(".rta-time").textContent = time;
    document.querySelector(".rta-date").textContent = `${day} ${formattedDate}`;
  };

  setInterval(updateDateTime, 1000);
});
