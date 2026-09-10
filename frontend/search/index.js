document.addEventListener("DOMContentLoaded", () => {
  loadAppointments();
});

async function loadAppointments() {
  try {
    const response = await fetch(
      "https://task-manager-basic-crud-production.up.railway.app/api/v1/appointments/",
    );

    const data = await response.json();

    const tbody = document.getElementById("appointments-table");

    tbody.innerHTML = "";

    data.forEach((appointment) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${appointment[0]}</td>
        <td>${appointment[1]}</td>
        <td>${appointment[2]}</td>
        <td>${appointment[3]}</td>
        <td>${appointment[4]}</td>


        <td>
            <button
                class="btn btn-warning"
                data-bs-toggle="modal"
                data-bs-target="#appointmentModal"
                data-id="${appointment.id}"
            >
                update
            </button>

            <button
                class="btn btn-danger delete-button"
                onclick="deleteAppointment(${appointment[0]})"
            >
                Delete
            </button>
        </td>
      `;

      tbody.appendChild(row);
    });
  } catch (error) {
    console.error("Erro:", error);
  }
}

async function deleteAppointment(id) {
  try {
    const response = await fetch(
      `https://task-manager-basic-crud-production.up.railway.app/api/v1/appointments/${id}`,
      {
        method: "DELETE",
      },
    );

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    loadAppointments();
  } catch (error) {
    console.error("Error:", error);
  }
}
