//Inicio do Codigo
var c = document.getElementById("canvas");
var ctx = c.getContext("2d");

var pri_linha = function(x_pri_linha, y_pri_linha, pri_linha_color, pri_linha_align, pri_linha_font, pri_linha_textSize, valor_inteiro){
    var de = "De";
    var por = "Por";
    ctx.font = pri_linha_font + pri_linha_textSize;
    ctx.fillText(de, x_pri_linha, y_pri_linha);
    var tam_de = ctx.measureText(de).width;
    ctx.font = "Arial Black" + pri_linha_textSize;
    ctx.fillText(valor_inteiro, x_pri_linha+tam_de, y_pri_linha);
}

var textUnderline = function(ctx,txt_valor_total,x,y,color,textSize,align){

    var textWidth = ctx.measureText(txt_valor_total).width;
    var startX = 0;
    var startY = y+(parseInt(textSize)/-3);
    var endX = 0;
    var endY = startY;
    var underlineHeight = parseInt(textSize)/10;

    if(underlineHeight < 1){
    underlineHeight = 1;
    }

    ctx.beginPath();
    if(align == "center"){
    startX = x - (textWidth/2);
    endX = x + (textWidth/2);
    }else if(align == "right"){
    startX = x-textWidth;
    endX = x;
    }else{
    startX = x;
    endX = x + textWidth;
    }

    ctx.strokeStyle = color;
    ctx.lineWidth = underlineHeight;
    ctx.moveTo(startX,startY);
    ctx.lineTo(endX,endY);ctx.strokeStyle = 'black';
    ctx.stroke();
}

var x_pri_linha = 50;
var y_pri_linha = 50; 
var pri_linha_color = "black"
var pri_linha_textSize = "50px"
var pri_linha_align = "center"
var pri_linha_font = "Arial"
var valor_inteiro = "R$ 4.200"

pri_linha(x_pri_linha, y_pri_linha, pri_linha_color, pri_linha_align, pri_linha_font, pri_linha_textSize, valor_inteiro)