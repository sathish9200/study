let vowels = ["a","e","i","o","u"];
// vowels.push("Finish");

let count = 0;
while(count < vowels.length)
{
    document.getElementById("output").innerHTML += vowels[count]  + "<br/>";
    count++;
}

// document.getElementById("output").innerHTML = vowels;

let marks = [55,65,37,87,95];

let total = 0;

for (let x=0; x<marks.length; x++){
    total = total + marks[x];
}
console.log(total);

let avg = total/marks.length;
console.log(avg);

document.getElementById("output").innerHTML += "<br/>" + "Marks = " + marks + "<br/>";
// document.getElementById("output").innerHTML += "<br/>" + marks + "<br/>";
document.getElementById("output").innerHTML += "<br/>" + "Total = " + total + "<br/>";
document.getElementById("output").innerHTML += "<br/>" + "Average = " + avg;
