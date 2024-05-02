const chk = document.getElementById('switch')

chk.addEventListener('change', () => {
  document.body.classList.toggle('dark')
})