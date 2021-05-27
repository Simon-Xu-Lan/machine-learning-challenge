window.onload = function () {
  var myCanvas = document.getElementById('myCanvas');
  console.log(myCanvas);
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

  var btnSave = document.getElementById('saveBtn');

  btnSave.addEventListener('click', function () {
    var imgURL = myCanvas.toDataURL('image/png');
    // GamepadButton.href = imgURL;
    // console.log(imgURL);

    // var image = myCanvas
    //   .toDataURL('image/png')
    //   .replace('image/png', 'image/octet-stream'); // here is the most important part because if you dont replace you will get a DOM 18 exception.

    // // window.location.href = image; // it will save locally

    // window.open(image, 'toDataURL() image', 'width=600, height=200');

    axios
      .post('/predict', {
        imgURL: imgURL,
      })
      .then(function (response) {
        // window.location.replace(`/result?model_output=${response['data']}`);
        console.log(response);
        document.getElementById("result").innerHTML = response.data
      })
      .catch(function (error) {
        console.log(error);
      });
  });
};
