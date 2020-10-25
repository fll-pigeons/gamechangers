var skulpt = new function() {
  var self = this;


  // Run on page load
  this.init = function() {
    Sk.configure({
      output: self.outf,
      read: self.builtinRead,
      __future__: Sk.python3
    });
    Sk.execLimit = 5000;
  };

  // Run program
  this.runPython = function(prog) {
    if (typeof self.hardInterrupt != 'undefined') {
      delete self.hardInterrupt;
    }
    if (self.running == true) {
      return;
    }
    self.running = true;

    var myPromise = Sk.misceval.asyncToPromise(
      function() {
        return Sk.importMainWithBody("<stdin>", false, prog, true);
      },
      {
        '*': self.interruptHandler
      }
    );
    var resetExecStart = setInterval(function(){Sk.execStart = Date();}, 2000);
    myPromise.then(
      function(mod) {
        self.running = false;
        clearInterval(resetExecStart);
        simPanel.setRunIcon('run');
      },
      function(err) {
        self.running = false;
        if (err instanceof Sk.builtin.ExternalError) {
          console.log(err.toString());
        } else {
          simPanel.consoleWriteErrors(err.toString());
        }
        clearInterval(resetExecStart);
        simPanel.setRunIcon('run');
      }
    );
  };

  // InterruptHandler
  this.interruptHandler = function (susp) {
    if (self.hardInterrupt === true) {
      delete self.hardInterrupt;
      throw new Sk.builtin.ExternalError('aborted execution');
    } else {
      return null;
    }
  };

  // Write to stdout
  this.outf = function (text) {
    simPanel.consoleWrite(text);
  }
  
  // File loader
  this.builtinRead = function (filename) {
    var externalLibs = {
      './ev3dev2/__init__.py': 'ev3dev2/__init__.py?v=1596843175',
      './ev3dev2/motor.py': 'ev3dev2/motor.py?v=1596843175',
      './ev3dev2/sound.py': 'ev3dev2/sound.py?v=1596843175',
      './pybricks/__init__.py': 'pybricks/__init__.py?v=1596843175',      
      './pybricks/ev3devices.py': 'pybricks/ev3devices.py?v=1596843175',   
      './pybricks/hubs.py': 'pybricks/hubs.py?v=1596843175',           
      './pybricks/media.py': 'pybricks/media.py?v=1596843175',   
      './pybricks/parameters.py': 'pybricks/parameters.py?v=1596843175',      
      './pybricks/robotics.py': 'pybricks/robotics.py?v=1596843175',   
      './pybricks/tools.py': 'pybricks/tools.py?v=1596843175',                  
      './ev3dev2/sensor/__init__.py': 'ev3dev2/sensor/__init__.py?v=1596843175',
      './ev3dev2/sensor/lego.py': 'ev3dev2/sensor/lego.py?v=1596843175',
      './ev3dev2/sensor/virtual.py': 'ev3dev2/sensor/virtual.py?v=1596843175',
      './simPython.js': 'js/simPython.js?v=1596843175'
    }
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][filename] === undefined) {
      if (filename in externalLibs) {
        return Sk.misceval.promiseToSuspension(
          fetch(externalLibs[filename])
            .then(r => r.text())
        );
      } else {
        throw "File not found: '" + filename + "'";
      }
    }
    return Sk.builtinFiles["files"][filename];
  };
}

// Init class
skulpt.init();
