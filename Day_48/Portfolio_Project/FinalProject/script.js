// Get references to DOM elements
const body=document.querySelector('body'),
      hourHand=document.querySelector('.hour'),
      minHand=document.querySelector('.minute'),
      secHand=document.querySelector('.second'),
      modeSwitch=document.querySelector('.mode-switch');
    //   add a click event listener to modeSwitch
    modeSwitch.addEventListener("click",()=>{
        body.classList.toggle('dark');
        const isDarkMode=body.classList.contains('dark');
        
    })

      const updateTime=()=>{
        // Get current time and calculate degrees for clock hands
        let date= new Date()
        secToDeg=(date.getSeconds()/60)*360,
        minToDeg=(date.getMinutes()/60)*360,
        hrToDeg=(date.getHours()/12)*360,
        // Rotate the clock hands to the appropriate degree based on the current time.
        secHand.style.transform=`rotate(${secToDeg}deg)`;
        minHand.style.transform=`rotate(${minToDeg}deg)`;
        hourHand.style.transform=`rotate(${hrToDeg}deg)`;
      };
//  call updateTime to set clock

setInterval(updateTime,1000);
    
updateTime();

// Other Web script

/*======================== toggle icon navbar ======================== */
let menuIcon= document.querySelector('#menu-icon');
let navbar= document.querySelector('.navbar');

menuIcon.onclick=() =>{
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};
 
/*======================== scroll sections avtive link ======================== */

let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a')

window.onscroll = () => {
    sections.forEach(sec =>{
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');
        if (top >= offset && top < offset + height){
            navLinks.forEach(links =>{
                links.classList.remove('active');
                document.querySelector('header nav a[href*= '+id+']').classList.add('active');
            });

        };
    });
    /*======================== sticky navbar ======================== */
    let header = document.querySelector('header');
    header.classList.toggle('sticky',window.scrllY>100);

    /*======================== remove toggle icon and navbar when click navbar link (scroll)======================== */
    menuIcon.classList.remove('bx-x');
    navbar.classList.remove('active');
    
};

/*======================== scroll reveal ======================== */

ScrollReveal({ 
    // reset: true,
    distance: '80px',
    duration: 2000,
    delay: 200
 });

 ScrollReveal().reveal('.home-content, .heading',{ origin:'top'});
 ScrollReveal().reveal('.home-img, .services-container.portfolio-box, .contactform',{ origin:'bottom'});
 ScrollReveal().reveal('.home-content h1, .about-img',{ origin:'left'});
 ScrollReveal().reveal('.home-content p, .about-content',{ origin:'right'});

 /*======================== typed js ======================== */
 const typed=new Typed('.multiple-text',{
    strings: ['Full Stack Web Developer','Full Stack Python Developer',],
    typeSpeed:100,
    backSpeed:50,
    backDelay:1000,
    loop:true
 });

