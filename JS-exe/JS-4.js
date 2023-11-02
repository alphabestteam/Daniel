
function starSign(date) {
    const month = date.getMonth() + 1; 
    const day = date.getDate();

    if ((month == 1 && day >= 21) || (month == 2 && day <= 19)) {
        console.log("Aquarius");
    } else if ((month == 2 && day >= 20) || (month == 3 && day <= 20)) {
        console.log("Pisces");
    } else if ((month === 3 && day >= 21) || (month == 4 && day <= 20)) {
        console.log("Aries");
    } else if ((month === 4 && day >= 21) || (month == 5 && day <= 21)) {
        console.log("Taurus");
    } else if ((month == 5 && day >= 22) || (month == 6 && day <= 21)) {
        console.log("Gemini");
    } else if ((month == 6 && day >= 22) || (month ==7 && day <= 22)) {
        console.log("Cancer");
    } else if ((month == 7 && day >= 23) || (month ==8 && day <= 23)) {
        console.log("Leo");
    } else if ((month == 8 && day >= 24) || (month == 9 && day <= 23)) {
        console.log("Virgo");
    } else if ((month == 9 && day >= 24) || (month == 10 && day <= 23)) {
        console.log("Libra");
    } else if ((month == 10 && day >= 24) || (month == 11 && day <= 22)) {
        console.log("Scorpio");
    } else if ((month == 11 && day >= 23) || (month == 12 && day <= 21)) {
        console.log("Sagittarius");
    } else {
        console.log("Capricorn");
    }
}

starSign(new Date("2022-03-25")); 
