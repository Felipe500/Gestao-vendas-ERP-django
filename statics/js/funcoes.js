
function response_add_item_venda(lista){
    var produto_list = ''
    console.log(lista)
    $("#table_produto tbody tr").remove()

    var table = document.getElementById("table_produto"),
    tbody = table.getElementsByTagName("tbody")[0];

    lista.forEach(function(produto){

        console.log(produto.itens[0])
        dt = produto.itens

         dt.forEach(function(item){
         console.log(item)
         var cell = document.createElement("td");
         var cellText = document.createTextNode('<tr>'+item+'</tr>');

            var row = document.createElement("tr");
            var cell = document.createElement("td");
            var cell2 = document.createElement("td");
            var cell3 = document.createElement("td");
            var cell4 = document.createElement("td");
            var cell5 = document.createElement("td");
            var cell6 = document.createElement("th");
            var cell6_a = document.createElement("a");
            var cell6_a_i = document.createElement("i");

            cell6_a_i.setAttribute("class", "fa fa-pencil")
            cell6_a.setAttribute("href", "/vendas/edit-item-pedido/"+item.id_item_pedido+"/")
            cell6.setAttribute("scope", "coll");

            cell6_a.appendChild(cell6_a_i)
            cell6.appendChild(cell6_a)

            var cell7 = document.createElement("th");
            var cell7_a = document.createElement("a");
            var cell7_a_i = document.createElement("i");

            cell7_a_i.setAttribute("class", "fa fa-window-close")
            cell7_a.setAttribute("href", "/vendas/delete-item-pedido/"+item.id_item_pedido+"/")
            cell7.setAttribute("scope", "coll");

            cell7_a.appendChild(cell7_a_i)
            cell7.appendChild(cell7_a)

            cell.innerHTML = item.produto_id;
            cell2.innerHTML = item.produto_name;
            cell3.innerHTML = item.produto_preco;
            cell4.innerHTML = item.quantidade;
            cell5.innerHTML = item.desconto;

            row.appendChild(cell);
            row.appendChild(cell2);
            row.appendChild(cell3);
            row.appendChild(cell4);
            row.appendChild(cell5);
            row.appendChild(cell6);
            row.appendChild(cell7);

            tbody.appendChild(row);

         });
       });

    }

function add_item_venda(id_venda){
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
            response_add_item_venda(result);
            $("#mensagem").text('produto incluido com sucesso');
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
            categoria_id: categoria_id
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