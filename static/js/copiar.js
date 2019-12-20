var copyTextareaBtn = document.querySelector('#id_copia');

copyTextareaBtn.addEventListener('click', function(event) {
  var copyTextarea = document.querySelector('.textarea');
  copyTextarea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'sim!' : 'não!';
  } catch (err) {
    alert('Opa, Não conseguimos copiar o texto, é possivel que o seu navegador não tenha suporte, tente usar Crtl+C.');
  }
});