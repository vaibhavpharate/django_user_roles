$(document).ready(()=>{
  $('.del_order_btn').click(function(){
    var order_id = $(this).attr('data-order');
    var product_name = $(this).attr('data-product');
    $('#del_link').attr('href',"delete_order/"+order_id);
    $('#product_name').html(product_name);
  })
})
