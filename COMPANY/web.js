function printer(){
    var copyd1=document.getElementById("headings").cloneNode(true);
    var copyd2=document.getElementById("copy").cloneNode(true);
    copyd2.innerHTML="Transport Copy";
    var copyd3=document.getElementById("tablebill").cloneNode(true);
    document.getElementById("fullbody").appendChild(copyd1);
    document.getElementById("fullbody").appendChild(copyd2);
    document.getElementById("fullbody").appendChild(copyd3);
    var copyd4=document.getElementById("headings").cloneNode(true);
    var copyd5=document.getElementById("copy").cloneNode(true);
    copyd5.innerHTML="Self Copy";
    var copyd6=document.getElementById("tablebill").cloneNode(true);
    document.getElementById("fullbody").appendChild(copyd4);
    document.getElementById("fullbody").appendChild(copyd5);
    document.getElementById("fullbody").appendChild(copyd6);
    window.print();
}