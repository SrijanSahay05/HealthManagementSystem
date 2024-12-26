document.addEventListener('DOMContentLoaded', () => {
  const tableBody = document.querySelector('.calendar-body tbody');

  // Populate the table dynamically
  for (let hour = 1; hour <= 24; hour++) {
    const row = document.createElement('tr');
    for (let day = 0; day < 7; day++) {
      const cell = document.createElement('td');
      cell.textContent = `${hour % 12 || 12} ${hour < 12 ? 'AM' : 'PM'}`;
      row.appendChild(cell);
    }
    tableBody.appendChild(row);
  }
});
