const requests = [
    { id: 1, name: "Paracetamol", quantity: "2 strips", patient: "Ravi Kumar" },
    { id: 2, name: "Amoxicillin", quantity: "1 strip", patient: "Sunita Verma" },
    { id: 3, name: "Metformin", quantity: "3 strips", patient: "Arjun Singh" }
  ];
  
  const container = document.getElementById("cardContainer");
  const statusText = document.getElementById("statusText");
  
  function showStatus(message) {
    statusText.textContent = message;
    statusText.style.opacity = 1;
  
    setTimeout(() => {
      statusText.style.opacity = 0;
    }, 2000);
  }
  
  function createCard(request) {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <h2>${request.name}</h2>
      <p><strong>Quantity:</strong> ${request.quantity}</p>
      <p><strong>Patient:</strong> ${request.patient}</p>
    `;
  
    let offsetX = 0;
  
    card.addEventListener("mousedown", startDrag);
    card.addEventListener("touchstart", startDrag);
  
    function startDrag(e) {
      e.preventDefault();
      let startX = e.type === "touchstart" ? e.touches[0].clientX : e.clientX;
  
      function onMove(ev) {
        let currentX = ev.type === "touchmove" ? ev.touches[0].clientX : ev.clientX;
        offsetX = currentX - startX;
        card.style.transform = `translateX(${offsetX}px) rotate(${offsetX * 0.05}deg)`;
      }
  
      function onEnd() {
        if (offsetX > 100) {
          card.style.transform = `translateX(1000px) rotate(30deg)`;
          card.style.transition = "transform 0.5s ease";
          showStatus(`✅ Accepted: ${request.name}`);
          setTimeout(() => card.remove(), 400);
        } else if (offsetX < -100) {
          card.style.transform = `translateX(-1000px) rotate(-30deg)`;
          card.style.transition = "transform 0.5s ease";
          showStatus(`❌ Rejected: ${request.name}`);
          setTimeout(() => card.remove(), 400);
        } else {
          card.style.transform = `translateX(0)`;
        }
  
        document.removeEventListener("mousemove", onMove);
        document.removeEventListener("mouseup", onEnd);
        document.removeEventListener("touchmove", onMove);
        document.removeEventListener("touchend", onEnd);
      }
  
      document.addEventListener("mousemove", onMove);
      document.addEventListener("mouseup", onEnd);
      document.addEventListener("touchmove", onMove);
      document.addEventListener("touchend", onEnd);
    }
  
    return card;
  }
  
  function renderCards() {
    for (let i = requests.length - 1; i >= 0; i--) {
      const card = createCard(requests[i]);
      container.appendChild(card);
    }
  }
  
  renderCards();
  