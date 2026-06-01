async function loadStats(){
  const res = await fetch('/stats');
  const data = await res.json();
  document.getElementById('cpu').innerText = data.cpu_percent + '%';
  document.getElementById('ram').innerText = data.memory_percent + '%';
  document.getElementById('system').innerText = data.system;
}
setInterval(loadStats,2000);
