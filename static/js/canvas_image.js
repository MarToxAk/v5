var textUnderline = function(ctx,text,x,y,color,textSize,align){

    var textWidth = ctx.measureText(text).width;
    var startX = 0;
    var startY = y+(parseInt(textSize)/-3);
    var endX = 0;
    var endY = startY;
    var underlineHeight = parseInt(textSize)/8;

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

    var text = "{{ dados.total }}";
    var textColor = "black";
    var fontSize = "45px";
    var fontFamily = "ArialBlack";
    var x = 104;
    var y = 679;
    var valor_total = "{{ dados.total }}";
    var valor_formatado = "{{ dados.val_diaria_format }}";
    var valor_porcentagem = "{{ dados.valor_disconto }}%";
    var canvas = document.getElementById("myCanvas");
    var ctx = canvas.getContext("2d");
    var img = new Image();
    ctx.font = "20px Georgia";


    img.onload = function() {
        ctx.drawImage(img, 0, 0);
        ctx.font = "45px ArialBlack";
        ctx.fillText(valor_formatado, 524 ,679);
        ctx.font = "30px ArialBlack";
        ctx.fillText(valor_formatado, 212, 931);
        ctx.fillText(valor_formatado, 211, 974);
        ctx.fillText(valor_formatado, 212, 1020);
        ctx.fillText(valor_porcentagem, 498, 1020);
      	ctx.font = fontSize + " " + fontFamily;
        ctx.fillStyle = textColor;
//Display the text on canvas
        ctx.fillText(text, x, y);
        textUnderline(ctx,text,x,y,textColor,fontSize);

//Call the function to underline the text
//We need to pass some values to our function so that it can

    }
