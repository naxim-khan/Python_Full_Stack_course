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