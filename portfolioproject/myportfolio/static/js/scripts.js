
function seleccionar(){
    //oculto el menu una vez que selecciono una opcion
    document.getElementById("navbar").classList = "";
    menuVisible = false;
}
//Funcion que aplica las animaciones de las habilidades
function efectoHabilidades(){
    var skills = document.getElementById("skills");
    var distancia_skills = window.innerHeight - skills.getBoundingClientRect().top;
    if(distancia_skills >= 300){
        let habilidades = document.getElementsByClassName("progreso");
        habilidades[0].classList.add("python");
        habilidades[1].classList.add("java");
        habilidades[2].classList.add("htmlcss");
        habilidades[3].classList.add("javascript");
        habilidades[4].classList.add("sql");
        habilidades[5].classList.add("comunicacion");
        habilidades[6].classList.add("trEquipo");
        habilidades[7].classList.add("creatividad");
        habilidades[8].classList.add("dedicacion");
        
    }
}


//detecto el scrolling para aplicar la animacion de la barra de habilidades
window.onscroll = function(){
    efectoHabilidades();
} 