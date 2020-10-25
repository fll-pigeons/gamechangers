var main = new function() {
  var self = this;

  // Run on page load
  this.init = function() {
    self.$navs = $('nav li');
    self.$panelControls = $('.panelControlsArea .panelControls');
    self.$panels = $('.panels .panel');
    self.$fileMenu = $('.fileMenu');
    self.$pythonMenu = $('.pythonMenu');
    self.$robotMenu = $('.robotMenu');
    self.$helpMenu = $('.helpMenu');

    self.$navs.click(self.tabClicked);
    self.$fileMenu.click(self.toggleFileMenu);
    self.$pythonMenu.click(self.togglePythonMenu);
    self.$robotMenu.click(self.toggleRobotMenu);
    self.$helpMenu.click(self.toggleHelpMenu);

    window.addEventListener('beforeunload', self.checkUnsaved);
    blocklyPanel.onActive();
  };

  // Save robot to json file
  this.saveRobot = function() {
    var hiddenElement = document.createElement('a');
    hiddenElement.href = 'data:application/json;base64,' + btoa(JSON.stringify(robot.options, null, 2));
    hiddenElement.target = '_blank';
    hiddenElement.download = robot.options.name + 'Robot.json';
    hiddenElement.dispatchEvent(new MouseEvent('click'));
  };

  // Load robot from json file
  this.loadRobot = function() {
    var hiddenElement = document.createElement('input');
    hiddenElement.type = 'file';
    hiddenElement.accept = 'application/json,.json';
    hiddenElement.dispatchEvent(new MouseEvent('click'));
    hiddenElement.addEventListener('change', function(e){
      var reader = new FileReader();
      reader.onload = function() {
        robot.options = JSON.parse(this.result);
        babylon.resetScene();
        skulpt.hardInterrupt = true;
        simPanel.setRunIcon('run');
        simPanel.initSensorsPanel();
      };
      reader.readAsText(e.target.files[0]);
    });
  };

  // About page
  this.openAbout = function() {
    let $body = $(
      '<div class="about">' +
        '<div></div>' +
        '<h3>Credits</h3>' +  
        '<p><a href="https://github.com/kendmaclean/gears_pybricks/" target="_blank">Gears Pybricks</a> is a fork of: <a href="https://quirkycort.github.io/gears/public/" target="_blank">Gearsbot</a></li></p>' + 
        '<p>which was created by Cort @ <a href="https://aposteriori.com.sg" target="_blank">A Posteriori</a>.</p>' +
        '<p>This simulator would not have been possible without the great people behind:</p>' +
        '<ul>' +
          '<li><a href="https://www.babylonjs.com/" target="_blank">Babylon.js</a></li>' +
          '<li><a href="https://developers.google.com/blockly" target="_blank">Blockly</a></li>' +
          '<li><a href="https://ace.c9.io/" target="_blank">Ace Editor</a></li>' +
          '<li><a href="https://skulpt.org/" target="_blank">Skulpt</a></li>' +
          '<li><a href="https://github.com/kripken/ammo.js/" target="_blank">Ammo.js</a> (port of <a href="https://pybullet.org/wordpress/" target="_blank">Bullet</a>)</li>' +
        '</ul>' +
        '<h3>License</h3>' +
        '<p>GNU General Public License v3.0</p>' +
        '<p>Gears Pybricks is a Free and Open Source Software</p>' +
      '</div>'
    );

    let $buttons = $(
      '<button type="button" class="confirm btn-success">Ok</button>'
    );

    let $dialog = dialog('About', $body, $buttons);

    $buttons.click(function(){
      console.log('f')
      $dialog.close();
    });
  };

  // Open page in new tab
  this.openPage = function(url) {
    window.open(url, '_blank');
  };

  // Toggle help
  this.toggleHelpMenu = function(e) {
    if ($('.helpMenuDropDown').length == 0) {
      $('.menuDropDown').remove();
      e.stopPropagation();

      let menuItems = [
        {html: 'Github', line: false, callback: function() { self.openPage('https://github.com/kendmaclean/gears_pybricks/'); }},
        {html: 'About', line: false, callback: self.openAbout }
      ];

      menuDropDown(self.$helpMenu, menuItems, {className: 'helpMenuDropDown'});
    }
  };

  // Select robot from templates
  this.selectRobot = function() {
    let $body = $('<div class="selectRobot"></div>');
    let $select = $('<select></select>');
    let $description = $('<div class="description"><img class="thumbnail"><div class="text"></div></div>');
    let $configurations = $('<div class="configurations"></div>');

    function displayRobotDescriptions(robot) {
      $description.find('.text').html(robot.longDescription);
      if (robot.thumbnail) {
        $description.find('.thumbnail').attr('src', robot.thumbnail);
      } else {
        $description.find('.thumbnail').attr('src', 'images/robots/default_thumbnail.png');
      }

      $configurations.html(robot.longerDescription);
    }

    robotTemplates.forEach(function(robotTemplate){
      let $robot = $('<option></option>');
      $robot.prop('value', robotTemplate.name);
      $robot.text(robotTemplate.shortDescription);
      if (robotTemplate.name == robot.options.name) {
        $robot.attr('selected', 'selected');
        displayRobotDescriptions(robotTemplate);
      }
      $select.append($robot);
    });

    $body.append($select);
    $body.append($description);
    $body.append($configurations);

    $select.change(function(){
      let robotTemplate = robotTemplates.find(robotTemplate => robotTemplate.name == $select.val());
      displayRobotDescriptions(robotTemplate);
    });

    let $buttons = $(
      '<button type="button" class="cancel btn-light">Cancel</button>' +
      '<button type="button" class="confirm btn-success">Ok</button>'
    );

    let $dialog = dialog('Select Robot', $body, $buttons);

    $buttons.siblings('.cancel').click(function() { $dialog.close(); });
    $buttons.siblings('.confirm').click(function(){
      robot.options = robotTemplates.find(robotTemplate => robotTemplate.name == $select.val());
      babylon.resetScene();
      skulpt.hardInterrupt = true;
      simPanel.setRunIcon('run');
      simPanel.initSensorsPanel();
      $dialog.close();
    });
  };

  // Display current position
  this.displayPosition = function() {
    let x = Math.round(robot.body.position.x * 10) / 10;
    let y = Math.round(robot.body.position.z * 10) / 10;
    let angles = robot.body.absoluteRotationQuaternion.toEulerAngles();
    let rot = Math.round(angles.y / Math.PI * 1800) / 10;

    acknowledgeDialog({
      title: 'Robot Position',
      message: $(
        '<p>Position: ' + x + ', ' + y + '</p>' +
        '<p>Rotation: ' + rot + ' degrees</p>'
      )
    })
  };

  // Save current position
  this.savePosition = function() {
    let x = Math.round(robot.body.position.x * 10) / 10;
    let y = Math.round(robot.body.position.z * 10) / 10;
    let angles = robot.body.absoluteRotationQuaternion.toEulerAngles();
    let rot = Math.round(angles.y / Math.PI * 1800) / 10;

    if (typeof babylon.world.defaultOptions.startPosXY != 'undefined') {
      babylon.world.options.startPosXY = x + ',' +y;
    } else {
      toastMsg('Current world doesn\'t allow saving of position');
      return;
    }
    if (typeof babylon.world.defaultOptions.startRot != 'undefined') {
      babylon.world.options.startRot = rot.toString();
    } else {
      toastMsg('Current world doesn\'t allow saving of rotation');
    }
    babylon.world.setOptions();
  };

  // Clear current position
  this.clearPosition = function() {
    if (babylon.world.options.startPosXY) {
      babylon.world.options.startPosXY = '';
    }
    if (babylon.world.options.startRot) {
      babylon.world.options.startRot = '';
    }
    babylon.world.setOptions();
  };


  // Toggle robot
  this.toggleRobotMenu = function(e) {
    if ($('.robotMenuDropDown').length == 0) {
      $('.menuDropDown').remove();
      e.stopPropagation();

      let menuItems = [
        {html: 'Select Robot', line: true, callback: self.selectRobot},
        {html: 'Load from file', line: false, callback: self.loadRobot},
        {html: 'Save to file', line: true, callback: self.saveRobot},
        {html: 'Display current position', line: false, callback: self.displayPosition},
        {html: 'Save current position to settings', line: false, callback: self.savePosition},
        {html: 'Clear position in settings', line: false, callback: self.clearPosition},
      ];

      menuDropDown(self.$robotMenu, menuItems, {className: 'robotMenuDropDown'});
    }
  };

  // Toggle python
  this.togglePythonMenu = function(e) {
    if ($('.pythonMenuDropDown').length == 0) {
      $('.menuDropDown').remove();
      e.stopPropagation();

      let menuItems = [
        {html: 'Pybricks Mode (Partial implementation)', line: false, callback: self.switchToPybricks}
      ];
      var tickIndex;
      if (blockly.generator == ev3dev2_generator) {
        tickIndex = 0;
      } else if (blockly.generator == pybricks_generator) {
        tickIndex = 1;
      }
      menuItems[tickIndex].html = '<span class="tick">&#x2713;</span> ' + menuItems[tickIndex].html;

      menuDropDown(self.$pythonMenu, menuItems, {className: 'pythonMenuDropDown'});
    }
  };

  this.switchToPybricks = function() {
    blockly.generator = pybricks_generator;
    blockly.generator.load();
  };

  // Toggle filemenu
  this.toggleFileMenu = function(e) {
    if ($('.fileMenuDropDown').length == 0) {
      $('.menuDropDown').remove();
      e.stopPropagation();

      let menuItems = [
        {html: 'New Program', line: true, callback: self.newProgram},
        {html: 'Load blocks from your computer', line: false, callback: self.loadFromComputer},
        {html: 'Import functions from blocks file', line: false, callback: self.importFunctionsFromFile},
        {html: 'Save blocks to your computer', line: true, callback: self.saveToComputer},
        {html: 'Load Python from your computer', line: false, callback: self.loadPythonFromComputer},
        {html: 'Save Python to your computer', line: true, callback: self.savePythonToComputer},
        {html: 'Export zip package to your computer', line: true, callback: self.saveZipToComputer},
      ];

      menuDropDown(self.$fileMenu, menuItems, {className: 'fileMenuDropDown'});
    }
  };

  // New program
  this.newProgram = function() {
    confirmDialog('Starting a new program will cause all unsaved work to be lost.', function() {
      blockly.loadDefaultWorkspace();
      pythonPanel.modified = false;
      localStorage.setItem('pythonModified', false);
      blocklyPanel.setDisable(false);
    });
  };

  // save Zip to computer
  this.saveZipToComputer = function() {
    var zip = new JSZip();
    zip.file('gearsBlocks.xml', blockly.getXmlText());
    if (pythonPanel.modified) {
      zip.file('gearsPython.py', pythonPanel.editor.getValue());
    } else {
      zip.file('gearsPython.py', blockly.generator.genCode());
    }
    zip.file('gearsRobot.json', JSON.stringify(robot.options, null, 2));

    zip.generateAsync({type:'base64'})
    .then(function(content) {
      var hiddenElement = document.createElement('a');
      hiddenElement.href = 'data:application/xml;base64,' + content;
      hiddenElement.target = '_blank';
      hiddenElement.download = 'gearsBot.zip';
      hiddenElement.dispatchEvent(new MouseEvent('click'));
    });
  };

  // save to computer
  this.saveToComputer = function() {
    var hiddenElement = document.createElement('a');
    hiddenElement.href = 'data:application/xml;base64,' + btoa(blockly.getXmlText());
    hiddenElement.target = '_blank';
    hiddenElement.download = 'gearsBot.xml';
    hiddenElement.dispatchEvent(new MouseEvent('click'));
  };

  // import functions from file
  this.importFunctionsFromFile = function() {
    var hiddenElement = document.createElement('input');
    hiddenElement.type = 'file';
    hiddenElement.accept = 'application/xml,.xml';
    hiddenElement.dispatchEvent(new MouseEvent('click'));
    hiddenElement.addEventListener('change', function(e){
      var reader = new FileReader();
      reader.onload = function() {
        blockly.importXmlTextFunctions(this.result);
        toastMsg('Functions imported');
      };
      reader.readAsText(e.target.files[0]);
    });
  };

  // load from computer
  this.loadFromComputer = function() {
    var hiddenElement = document.createElement('input');
    hiddenElement.type = 'file';
    hiddenElement.accept = 'application/xml,.xml';
    hiddenElement.dispatchEvent(new MouseEvent('click'));
    hiddenElement.addEventListener('change', function(e){
      var reader = new FileReader();
      reader.onload = function() {
        blockly.loadXmlText(this.result);
      };
      reader.readAsText(e.target.files[0]);
    });
  };

  // save to computer
  this.savePythonToComputer = function() {
    var hiddenElement = document.createElement('a');
    hiddenElement.href = 'data:text/x-python;base64,' + btoa(pythonPanel.editor.getValue());
    hiddenElement.target = '_blank';
    hiddenElement.download = 'gearsBot.py';
    hiddenElement.dispatchEvent(new MouseEvent('click'));
  };

  // load from computer
  this.loadPythonFromComputer = function() {
    var hiddenElement = document.createElement('input');
    hiddenElement.type = 'file';
    hiddenElement.accept = 'text/x-python,.py';
    hiddenElement.dispatchEvent(new MouseEvent('click'));
    hiddenElement.addEventListener('change', function(e){
      var reader = new FileReader();
      reader.onload = function() {
        pythonPanel.editor.setValue(this.result, 1);
        self.tabClicked('navPython');
        pythonPanel.warnModify();
      };
      reader.readAsText(e.target.files[0]);
    });
  };

  // Check for unsaved changes
  this.checkUnsaved = function (event) {
    if (blockly.unsaved || pythonPanel.unsaved) {
      event.preventDefault();
      event.returnValue = '';
    }
  };

  // Clicked on tab
  this.tabClicked = function(tabNav) {
    if (typeof tabNav == 'string') {
      var match = tabNav;
    } else {
      var match = $(this)[0].id;
    }

    function getPanelByNav(nav) {
      if (nav == 'navBlocks') {
        return blocklyPanel;
      } else if (nav == 'navPython') {
        return pythonPanel;
      } else if (nav == 'navSim') {
        return simPanel;
      }
    };

    inActiveNav = self.$navs.siblings('.active').attr('id');
    inActive = getPanelByNav(inActiveNav);
    active = getPanelByNav(match);

    self.$navs.removeClass('active');
    $('#' + match).addClass('active');

    self.$panels.removeClass('active');
    self.$panels.siblings('[aria-labelledby="' + match + '"]').addClass('active');

    self.$panelControls.removeClass('active');
    self.$panelControls.siblings('[aria-labelledby="' + match + '"]').addClass('active');

    if (typeof inActive.onInActive == 'function') {
      inActive.onInActive();
    }
    if (typeof active.onActive == 'function') {
      active.onActive();
    }
  };
}

// Init class
main.init();
