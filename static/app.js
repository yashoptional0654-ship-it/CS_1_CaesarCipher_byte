let mode = 'encrypt';

function setMode(m){
  mode = m;
  document.getElementById('modeEnc').setAttribute('aria-pressed', m === 'encrypt');
  document.getElementById('modeDec').setAttribute('aria-pressed', m === 'decrypt');
  run();
}

async function run(){
  const text = document.getElementById('input').value;
  const shift = document.getElementById('shift').value;
  const errorEl = document.getElementById('errorMsg');
  const outputEl = document.getElementById('output');
  errorEl.textContent = '';

  try{
    const res = await fetch('/api/process', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, mode, shift })
    });
    const data = await res.json();
    if(!res.ok){
      errorEl.textContent = data.error || 'Something went wrong.';
      outputEl.textContent = '';
      return;
    }
    outputEl.textContent = data.result;
  }catch(err){
    errorEl.textContent = 'Could not reach the server. Please try again.';
  }
}

document.getElementById('input').addEventListener('input', run);
document.getElementById('shift').addEventListener('input', run);

run();
