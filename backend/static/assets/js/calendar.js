const today = new Date();
today.setDate(today.getDate() + 1);
const dd = String(today.getDate()).padStart(2, '0');
const mm = String(today.getMonth() + 1).padStart(2, '0');
const yyyy = today.getFullYear();
const formattedDate = yyyy + '-' + mm + '-' + dd;
document.getElementById('date').setAttribute('min', formattedDate);