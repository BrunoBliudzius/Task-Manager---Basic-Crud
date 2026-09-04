document.addEventListener("DOMContentLoaded", () => {
  loadAppointments();
});

async function loadAppointments() {
  try {
    const response = await fetch(
      "https://task-manager-basic-crud-production.up.railway.app/appointments/",
    );

    const data = await response.json();

    const tbody = document.getElementById("appointments-table");

    data.forEach((appointment) => {
      const row = document.createElement("tr");
      row.innerHTML = `<td>${appointment.id}</td>
                    <td>${appointment.title}</td>
                    <td>${appointment.description}</td>
                    <td>${appointment.date}</td>
                    <td>${appointment.end_time}</td>
                    <td>
                    <a class="btn btn-sm btn-primary" href="#"> Update </a>
                    <a class="btn btn-sm btn-danger" href="#"> Delete </a>
                    </td> `;

      tbody.appendChild(row);
    });
  } catch (error) {
    console.error("Erro:", error);
  }
}
