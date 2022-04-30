function PostMaqCartao() {
  var post = validateForm();

  alert(post);

  if (post == true) {
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $.ajax({
        type: 'POST',
        url: '/vendas/add_item_list',
        data: {
            csrfmiddlewaretoken: token,
            name_maq: $('#cre1').val(),
            deb: $('#debito').val(),
            cre1: $('#cre1').val(),
            cre2: $('#cre2').val(),
            cre3: $('#cre3').val(),
            cre4: $('#cre4').val(),
            cre5: $('#cre5').val(),
            cre6: $('#cre6').val(),
            cre7: $('#cre7').val(),
            cre8: $('#cre8').val(),
            cre9: $('#cre9').val(),
            cre10: $('#cre10').val(),
            cre11: $('#cre11').val(),
            cre12: $('#cre12').val(),

        },
        success: function(result){
            alert('ok');
            response_add_item_venda(result);
            $("#mensagem").text('produto incluido com sucesso');
        }
    });

  }



}

function validateForm() {
  var post = true;

if($('#name').val() == ''){
      alert('nome');
        post = false;
   }
if($('#debito').val() == ''){
      alert('debito');
        post = false;
   }
 if($('#cre1').val() == ''){
      alert('credito x1');
        post = false;
   }

if($('#cre2').val() == ''){
      alert('credito x2');
        post = false;
   }

if($('#cre3').val() == ''){
      alert('credito x3');
        post = false;
   }

if($('#cre4').val() == ''){
      alert('credito x4');
        post = false;
   }

if($('#cre5').val() == ''){
      alert('credito x5');
        post = false;
   }

if($('#cre6').val() == ''){
      alert('credito x6');
        post = false;
   }


if($('#cre7').val() == ''){
      alert('credito x7');
        post = false;
   }

if($('#cre8').val() == ''){
      alert('credito x8');
        post = false;
   }

if($('#cre9').val() == ''){
      alert('credito x9');
        post = false;
   }

if($('#cre10').val() == ''){
      alert('credito x10');
        post = false;
   }

if($('#cre11').val() == ''){
      alert('credito x11');
        post = false;
   }

if($('#cre12').val() == ''){
      alert('credito x12');
        post = false;
   }

if($('#cre2').val() == ''){
      alert('credito x2');
        post = false;
   }
 return post

}

function add_item_venda(){
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    id_produto = document.getElementById("id_produto_list").value;
    desconto_produto = document.getElementById("desconto_produto").value;
    quantidade_produto = document.getElementById("id_quantidade").value;


    console.log('produto: '+id_produto);
    console.log('quantidade: '+quantidade_produto);
    console.log('desconto: '+desconto_produto);
    console.log(id_venda);
    $.ajax({
        type: 'POST',
        url: '/vendas/add_item_list',
        data: {
            csrfmiddlewaretoken: token,
            venda_id: id_venda,
            id_produto: id_produto,
            desconto_produto: desconto_produto,
            quantidade_produto: quantidade_produto

        },
        success: function(result){
            alert('ok');
            response_add_item_venda(result);
            $("#mensagem").text('produto incluido com sucesso');
        }
    });
}