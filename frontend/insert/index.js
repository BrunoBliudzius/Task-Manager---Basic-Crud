const form = document.querySelector("form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const appointment = {
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
    date: document.getElementById("start_date").value,
    end_time: document.getElementById("end_date").value,
  };

  try {
    const response = await fetch("http://127.0.0.1:8000/appointments/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(appointment),
    });

    const data = await response.json();
    alert(data.message);

  } catch (error) {
    console.error("Erro:", error);
  }
});
