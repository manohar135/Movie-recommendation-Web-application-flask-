let header = document.querySelector("header");

window.addEventListener("scroll", () => {
  header.classList.toggle("shadow", window.scrollY > 100);
});


// sending the input to flask app and geting the 5 movie list
function filterFunction(rec) { //When recommend botton is clicked
  var input = document.getElementById("myInput").value;
  var data = { str: input, is_rec: rec};

  fetch("/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.text())
    .then((data) => {
      if(rec){
        displayRecommendation(JSON.parse(data))
        // displayRecommendation(data)
      }else{
        displayFilter(JSON.parse(data));
      }
    });
}


//Displaying the movie list on to the web page
function displayFilter(data) {
  ul = document.getElementById("movieList");

  //remove old list
  while (ul.firstChild) {
    ul.removeChild(ul.lastChild);
  }

  for (var i = 0; i < data.length; i++) {
    var li = document.createElement("li");
    li.classList.add("list-group-item");
    li.textContent = data[i]; // Set the text content of <li> to the current item
    ul.appendChild(li); // Append the <li> to the <ul>
  }

  //Getting the title name on Click
  var listItems = document.getElementsByClassName("list-group-item");

  for (var i = 0; i < listItems.length; i++) {
    listItems[i].addEventListener("click", function () {

      while (ul.firstChild) {
        ul.removeChild(ul.lastChild);
      }

      var name = this.textContent; 
      document.getElementById("myInput").value = name;
    });
  }
}


function displayRecommendation(data){
  cardImage = document.getElementsByClassName("card-img-top");
  cardTitles = document.getElementsByClassName("card-title");
  for(var i = 0; i<cardTitles.length; i++){
    cardImage[i].src = data.posters[i]
    cardTitles[i].textContent = data.titles[i];
  }
}

