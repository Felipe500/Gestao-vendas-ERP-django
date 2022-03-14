

function add_item_venda(value){
    venda_id = value;
    console.log(venda_id);
    $.ajax({
        type: 'GET',
        url: '/add_item_list/',
        data: {
            venda_id: categoria_id
        },
        success: function(result){
            process_response(result);
            $("#mensagem").text('Funcionarios carregados');
        }
    });
}
function alerta(){
    alert("rodou!!!!!!!!!!");

}
function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
            outro_param: 123
        },
        success: function(result){
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}




function process_response(produtos){
    func_select = document.getElementById('id_produto_list');
    func_select.innerHTML = "";






    produtos.forEach(function(produto){
        var option = document.createElement("option");
        option.text = produto.fields.descricao;
        option.value = produto.pk;
        func_select.add(option);
    });


}


function filtra_produtos(value){
    categoria_id = value;
    console.log(categoria_id);
    $.ajax({
        type: 'GET',
        url: '/filtra_produtos/',
        data: {
            outro_param: categoria_id
        },
        success: function(result){
            process_response(result);
            $("#mensagem").text('Funcionarios carregados');
        }
    });
}




function myFunction(value) {
    id_catgoria1 = value;
    console.log(id_catgoria1);
}