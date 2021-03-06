window.onload = function () {


  var myCanvas = document.getElementById('myCanvas');
  var ctx = myCanvas.getContext('2d');

  // Fill window width and Height
  myCanvas.width = 400; // window.innerWidth;
  myCanvas.height = 400; //window.innerHeight * 0.6;

  // Set Background color
  ctx.fillStyle = '#fff';
  ctx.fillRect(0, 0, myCanvas.width, myCanvas.height);

  // Mouse event handler
  if (myCanvas) {
    var isDown = false;
    var canvasX, canvasY;
    ctx.lineWidth = 20;
    ctx.lineCap = "round"

    $(myCanvas)
      .mousedown(function (e) {
        isDown = true;
        ctx.beginPath();
        canvasX = e.pageX - myCanvas.offsetLeft;
        canvasY = e.pageY - myCanvas.offsetTop;
        ctx.moveTo(canvasX, canvasY);
      })
      .mousemove(function (e) {
        if (isDown != false) {
          canvasX = e.pageX - myCanvas.offsetLeft;
          canvasY = e.pageY - myCanvas.offsetTop;
          ctx.lineTo(canvasX, canvasY);
          ctx.strokestyle = '#000';
          ctx.stroke();
        }
      })
      .mouseup(function (e) {
        isDown = false;
        ctx.closePath();
      });
  }

  // Touch Events Handlers
  draw = {
    started: false,
    start: function (event) {
      ctx.beginPath();
      ctx.moveTo(event.touches[0].pageX, event.touches[0].pageY);
      this.started = true;
    },

    move: function (event) {
      if (this.started) {
        ctx.lineTo(event.touches[0].pageX, event.touches[0].pageY);

        ctx.strokestyle = '#000';
        ctx.lineWidh = 10;
        ctx.stroke();
      }
    },

    end: function (event) {
      this.started = false;
    },
  };

  // Touch events
  myCanvas.addEventListener('touchstart', draw.start, false);
  myCanvas.addEventListener('touchend', draw.end, false);
  myCanvas.addEventListener('touchmove', draw.move, false);

  // Disable Page Move
  document.body.addEventListener(
    'touchmove',
    function (event) {
      event.preventDefault();
    },
    false
  );

  // Change line width
  // var lineWidthSelect = document.getElementById("linewidth")
  // lineWidthSelect
  //   .addEventListener("change", function() {
  //     ctx.lineWidh = lineWidthSelect.value
  //     // window.location.reload()
  //   })



  // Reset white board
  document
    .getElementById("reset")
    .addEventListener('click', function () {
      window.location.reload()
    })

  // Button A is clicked
  var btnA = document.getElementById('btnA');

  btnA.addEventListener('click', function () {
    var imgURL = myCanvas.toDataURL('image/png');

    axios
      .post('/', {
        imgURL: imgURL,
        scenario: "A", // Scenario A: There is one number on the board
      })
      .then(function (response) {
        // window.location.replace(`/result?model_output=${response['data']}`);
        console.log(response);
        document.getElementById("result").innerHTML = response.data[0]
        document.getElementById("imgA").src = response.data[1]
        document.getElementById("result1").style.display="block"
        document.getElementById("prediction1").value=response.data[0]

      })
      .catch(function (error) {
        console.log(error);
      });
  });

  // Button B is clicked
  var btnB = document.getElementById('btnB');

  btnB.addEventListener('click', function () {
    var imgURL = myCanvas.toDataURL('image/png');

    axios
      .post('/', {
        imgURL: imgURL,
        scenario: "B", // Scenario B: There is two numbers on the board
      })
      .then(function (response) {
        // window.location.replace(`/result?model_output=${response['data']}`);
        console.log(response);
        var first = response.data[0]
        var second = response.data[1]
        document.getElementById("result").innerHTML = first + second
        document.getElementById("imgA").src = response.data[2]
        document.getElementById("imgB").src = response.data[3]
        document.getElementById("result1").style.display="block"
        document.getElementById("result2").style.display="block"
        document.getElementById("prediction1").value=first
        document.getElementById("prediction2").value=second
      })
      .catch(function (error) {
        console.log(error);
      });
  });


  // Save button is clicked
  var saveBtn1 = document.getElementById("savebtn1")
  saveBtn1.addEventListener('click', function() {
    var prediction1 = document.getElementById("prediction1").value
    var imgURLA = document.getElementById("imgA").src
    if (saveBtn1.innerHTML !== "SAVED") {
      axios
        .post('/', {
          imgURL: imgURLA,
          prediction: prediction1,
          scenario: "SAVE", // Scenario SAVE
        })
        .then(function (response) {
          // window.location.replace(`/result?model_output=${response['data']}`);
          console.log(response);
          saveBtn1.innerHTML ="SAVED"
          saveBtn1.style.background = "darkgray"
          saveBtn1.style.color ="red"
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  })

  var saveBtn2 = document.getElementById("savebtn2")
  saveBtn2.addEventListener('click', function() {
    var prediction2 = document.getElementById("prediction2").value
    var imgURLB = document.getElementById("imgB").src
    if (saveBtn2.innerHTML !== "SAVED") {
      axios
        .post('/', {
          imgURL: imgURLB,
          prediction: prediction2,
          scenario: "SAVE", // Scenario SAVE
        })
        .then(function (response) {
          // window.location.replace(`/result?model_output=${response['data']}`);
          console.log(response);
          saveBtn2.innerHTML ="SAVED"
          saveBtn2.style.background = "darkgray"
          saveBtn2.style.color ="red"
        })
        .catch(function (error) {
          console.log(error);
        });
    }

  })


};
