const selfDrivingBtn = document.getElementById('self-driving-btn');
const needSeatBtn = document.getElementById('need-seat-btn');
const formContainer = document.getElementById('form-container');
const tableContainer = document.getElementById('table-container');
const selfDrivingForm = document.getElementById('self-driving-form');
const carSeatsTable = document.getElementById('car-seats-table');

let carSeatsData = [];


function loadData() {
 fetch('data.json')
    .then(response => response.json())
    .then(data => {
      carSeatsData = data;
      renderTable();
    })
    .catch(error => console.log(error));
}

function renderTable() {
 const tbody = carSeatsTable.querySelector('tbody');
 tbody.innerHTML = '';

 carSeatsData.forEach((seat, index) => {
    const row = document.createElement('tr');
  
    const nameCell = document.createElement('td');
    nameCell.textContent = seat.name;
    row.appendChild(nameCell);

    const seatsCell = document.createElement('td');
    seatsCell.textContent = seat.seats;
    row.appendChild(seatsCell);

    const actionCell = document.createElement('td');
    if (seat.seats > 0) {
      const button = document.createElement('button');
      button.textContent = 'Select';
      button.addEventListener('click', () => {
        seat.seats--;
        if (seat.seats === 0) {
          carSeatsData.splice(index, 1);
        }
        renderTable();
      });
      actionCell.appendChild(button);
    }
    row.appendChild(actionCell);

    tbody.appendChild(row);
  });
}

selfDrivingBtn.addEventListener('click', () => {
 formContainer.classList.remove('hidden');
 tableContainer.classList.add('hidden');
});

needSeatBtn.addEventListener('click', () => {
 formContainer.classList.add('hidden');
 tableContainer.classList.remove('hidden');
 loadData();
});

selfDrivingForm.addEventListener('submit', event => {
  event.preventDefault();

 const name = event.target.name.value.trim();
 const seats = parseInt(event.target.seats.value, 10);

  if (name && seats > 0) {
    carSeatsData.push({ name, seats });
    renderTable();
    formContainer.classList.add('hidden');
    tableContainer.classList.remove('hidden');
  }
});

loadData();