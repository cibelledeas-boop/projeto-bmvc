
function mascaraCPF(v){
  v=v.replace(/\D/g,'');
  v=v.replace(/(\d{3})(\d)/,'$1.$2');
  v=v.replace(/(\d{3})(\d)/,'$1.$2');
  v=v.replace(/(\d{3})(\d{1,2})$/,'$1-$2');
  return v.slice(0,14);
}

function validarCPF(cpf){
  cpf = cpf.replace(/\D/g,'');
  if(cpf.length!==11 || /^(\d)\1{10}$/.test(cpf)) return false;
  let soma=0;let resto;
  for(let i=1;i<=9;i++) soma += parseInt(cpf.substring(i-1,i))*(11-i);
  resto = (soma*10)%11; if(resto===10||resto===11)resto=0; if(resto!==parseInt(cpf.substring(9,10)))return false;
  soma=0;
  for(let i=1;i<=10;i++) soma += parseInt(cpf.substring(i-1,i))*(12-i);
  resto = (soma*10)%11; if(resto===10||resto===11)resto=0; if(resto!==parseInt(cpf.substring(10,11)))return false;
  return true;
}

document.addEventListener('DOMContentLoaded',()=>{
  const cpf = document.getElementById('cpf');
  const senha = document.getElementById('senha');
  const toggle = document.getElementById('toggleSenha');
  const form = document.getElementById('loginForm');
  const lembrar = document.getElementById('lembrar');

  
  const savedCpf = localStorage.getItem('rememberCPF');
  if(savedCpf){
    cpf.value = savedCpf;
    lembrar.checked = true;
  }

  cpf.addEventListener('input',()=>{cpf.value = mascaraCPF(cpf.value)});

  toggle.addEventListener('click',()=>{
    if(senha.type==='password'){senha.type='text';toggle.textContent='🙈';}
    else{senha.type='password';toggle.textContent='👁️';}
  });

  form.addEventListener('submit',(e)=>{
    e.preventDefault();
    const rawCpf = cpf.value.replace(/\D/g,'');
    if(!validarCPF(cpf.value)){
      alert('CPF inválido. Verifique e tente novamente.');
      cpf.focus();
      return;
    }
    if(!senha.value || senha.value.length<4){
      alert('Informe sua senha (mínimo 4 caracteres).');
      senha.focus();
      return;
    }

 
    if(lembrar.checked){
      localStorage.setItem('rememberCPF', cpf.value);
    } else {
      localStorage.removeItem('rememberCPF');
    }


    const session = {cpf: rawCpf, loggedAt: new Date().toISOString()};
    localStorage.setItem('session', JSON.stringify(session));

    alert('Login realizado (simulado).');
   
  });
});
