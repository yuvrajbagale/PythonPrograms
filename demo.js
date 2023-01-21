/*
    - This is the custom coding interface for Sleave. 
    
    - You can create your custom functions and call them from Action Panel interface

    - To avoid any conflict with core code
        * start your function names with 'cust_'
        * start your variable names with 'c_'

    - You can also access objects using the dot notation, there are 3 containers
        - _top (header)
        - _stage (Content area, stage)
        - _bottom (footer)
        Each of these containers has a property 'objects' which can be used to access its children
        Example:
                - _stage.L8		(Object is in main timeline)
                - _stage.C1.L2 	(Object is inside Clip C1)

        You can then manipulate all javascript/CSS properties of the object. Go through the help to see what methods are provided by Sleave API.
*/

//Gets called when user performs a swipe on touch device
function cust_swipeEvent(evnt, swipedirection) {
    //f_log(evnt.clientX+", "+evnt.clientY)
  }
  
  //called when one of the child windows is closed
  function cust_ChildWindowClosed(){
  
  }
  
  function a_changetopbar(ref,evt,param)
  {
  _top.goToLabel(param)
  }
  
  var playBtnState;
  function a_disablePlayBtn(){
  
  playBtnState = 0;
  _bottom.button_bar.goToLabel("l_pause");
  }
  
  
  function a_enablePlayBtn(){
  
  playBtnState = 1;
  _bottom.button_bar.goToLabel("l_play");
  }
  
  function a_enablePlayBtn2(){
  
  playBtnState = 1;
  f_log(_stage.currentFrame()+"="+_stage.lastFrame())
  if(!_audio.hasEnded)
    {
    _bottom.button_bar.goToLabel("l_play");
    }
  }
  
  function FinishSimulation(){
  if(typeof f_lmsaction === "function"){
  f_lmsaction("finish");
    }
  }
  
  function a_getPlayBtnState(ref){
  
  if(playBtnState == 0){
      ref.disable();
  
    }else{
      ref.enable();
      ref.getFocus();
    }
  
  }
  
  function c(ref,evt,param)
  {
  _top.goToLabel(param)
  }
  
  
  function a_showHideTranscript(ref,evt,param){
  
  var bool = parseInt(param,10);
  
  if(bool == 2){
    bool = _bottom.transcriptmc.currentLabel() == "l_hide"?1:0;
  }
  
  if(!bool){
    //Hide
    _bottom.transcriptmc.goToLabel("l_hide");
    _bottom.button_bar.moveTo(735,-82,500,"ease");
        //_bottom.button_bar.transcript_btn.getFocus()
    _bottom.button_bar.transcript_btn.enable()
  }else{
    //show
    _bottom.button_bar.transcript_btn.disable()
    _bottom.transcriptmc.goToLabel("l_show");
        _bottom.button_bar.moveTo(285,-82,500,"ease");
  }
  }
  
  
  //
  function checkHint(ref,evt,param1){
   
    var qz=_quiz[_course.moduleID][_course.pageID+param1];
  var tryies = qz.attempts;
    _stage.hintmc.goToLabel("h"+tryies);
  }
  
  function bottomBarState(ref,event,param){
  if(param === "0"){
    if (_bottom && _bottom.patchmc && _bottom.patchmc._init) _bottom.patchmc.goToLabel("show");
    if (_top && _top.patchmc && _top.patchmc._init) _top.patchmc.goToLabel("show");
  }else{
    if (_bottom && _bottom.patchmc && _bottom.patchmc._init) _bottom.patchmc.goToFrame(1);
   if (_top && _top.patchmc && _top.patchmc._init) _top.patchmc.goToFrame(1);
  }
  }
  
  
  
  //Gets called whenever mouse moves
  function cust_MouseMove(evnt, swipedirection) {
    //f_log(evnt.clientX+", "+evnt.clientY)
  }
  
  //Gets called on Pagescroll
  function cust_PageScroll(ref) {
  
  }
  
  //Gets called on Mousedown anywhere on the page
  function cust_MouseDown() {
  
  }
  //Gets called when a frame is rendered
  function cust_exitFrame(tlref){
  
  }
  //Gets called when a voiceover audio starts
  function cust_audioStarted(ref,src){
    
  }
  //Gets called whenever a key is pressed
  function cust_KeyDown(evnt) {
    //f_log(evnt.keyCode)
  }
  
  function cust_PageCompleted(){
  /*
  if(_top && _top.C4){
    var prg=_course.getCourseProgress()/100
    _top.C4.H2.scaleTo(prg,1,500,"ease")
  }*/
  }
  
  //Gets called when page loading starts
  function cust_PageLoadBegin() {
  if(_top && _top.Button_Cutout){
    _top.Button_Cutout.show()
  }
  bottomBarState(null,null,"1");
    playBtnState = 1;
  if(_bottom && _bottom.readyfornextscreen && _bottom.readyfornextscreen._init){
    _bottom.readyfornextscreen.goToLabel("l_0");
  }
  
  
  
  }
  
  var a_nTotalPages;
  function getTotalPages(){
  var aTemp = [];
  var prevNum;
  var highNum = 0;
  _top.T1.setRendering(0);
  var allData = _top.T1.records.data;
  for(var i=0;i<allData.length;i++){
    var temp = _util.trim(allData[i][1]);
    temp = temp.split("&nbsp;").join("");
    prevNum = parseInt(temp,10);
  if(prevNum > highNum){
      highNum = prevNum
    }
  }
  
  
  a_nTotalPages = highNum;
  }
  
  //Gets called when a page is loaded
  function cust_PageLoaded() {
    if(_top && _top.Button_Cutout){
      setTimeout(function(){_top.Button_Cutout.hide()},1000)
    }
  if(_top && _top.C4){
     var res = _top.T1.records.find("pageId", _course.pageID,0);
    res = _util.trim(res[0][1])
        res = res.split("&nbsp;").join("");
   _top.a_pageCount.setContent(res+" of "+a_nTotalPages);
  //    var prg=_course.getPageNumInCourse()/_course.totalPages
        var prg= parseInt(res,10)/a_nTotalPages*100;
    f_log(prg*2)
    _top.C4.H2.sizeTo(prg*2,16,500,"ease")
  
  }
  
  
  
  
  if(_bottom && _bottom.C2){
    _bottom.C2.goToFrame(2)
  }
  //bottomBarState(null,null,"1");
  
  
  }
  function cust_WindowResized(){
    
  }
  
  function cust_ExitCourse() {
  
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  //---------------------------------------Glossary Code Start------------------------------------------------//
  var g_data
  
  function cust_btnRender(ref) {
    var i
    for (i = 1; i <= 30; i++) {
        ref["term_" + i].setRendering(0)
    }
    var c_data = ref.T6.records.data
    var n_letter = [],
        chr
    for (i = 0; i < c_data.length; i++) {
        chr = c_data[i][0]
        if (n_letter.indexOf(chr) === -1) {
            n_letter.push(chr)
            ref["l_" + chr].enable()
        }
    }
    g_data = ref.T6.records.find("displayin", n_letter[0], 0)
    for (i = 1; i <= g_data.length; i++) {
        ref["term_" + i].setRendering(1)
        ref["term_" + i].setContent(g_data[i - 1][1])
    }
    ref["l_" + n_letter[0]].select()
    ref.L2.setContent(g_data[0][2])
    var c_dwidth = _device.width
    var c_str
  
    //------------------Hide inactive Alphabat buttons for smaller devices
    if (c_dwidth <= 550) {
        for (i = 97; i <= 122; i++) {
            c_str = String.fromCharCode(i)
            if (ref["l_" + c_str].isdisabled) {
                ref["l_" + c_str].setRendering(0)
            }
        }
    }
    //-------------------Hide Inactive button end----------------
  }
  
  function cust_getTerms(ref) {
    var i
    var btn_id = ref.layerName.split("_")[1]
    ref = _top[ref.timeline]
    for (i = 1; i <= 30; i++) {
        ref["term_" + i].setRendering(0)
    }
  
    g_data = ref.T6.records.find("displayin", btn_id, 0)
    for (i = 1; i <= g_data.length; i++) {
        ref["term_" + i].setRendering(1)
        ref["term_" + i].setContent(g_data[i - 1][1])
    }
    ref.L2.setContent(g_data[0][2])
  }
  
  function cust_getDesc(ref) {
    var btn_id1 = ref.layerName.split("_")[1]
    ref = _top[ref.timeline]
    btn_id1 = parseInt(btn_id1, 10) - 1
    ref.L2.setContent(g_data[btn_id1][2])
  }
  
  function cust_showGlossary() {
    var lbl = _top.glossary.currentLabel()
    _bottom.transcript.goToLabel("l_hide")
    _bottom.button_bar.transcript_btn.reset()
    _top.glossary.goToLabel(lbl == "l_show" ? "l_hide" : "l_show")
  }
  
  function cust_showTranscript() {
    var lbl = _bottom.transcript.currentLabel()
    _top.glossary.goToLabel("l_hide")
    _bottom.button_bar.glossary_btn.reset()
    _bottom.transcript.goToLabel(lbl == "l_show" ? "l_hide" : "l_show")
  }
  
  function cust_btnReset() {
    _bottom.button_bar.glossary_btn.reset()
    _bottom.button_bar.transcript_btn.reset()
  }
  //---------------------------------------Glossary Code End------------------------------------------------//
  
  function cust_intclicked(modref, pgref, intref, btnref) {
    f_log("Module " + modref + ", page " + pgref + " Interaction " + intref + " button " + btnref)
    if (modref == "module03" && pgref == "p02") {
        switch (intref) {
            case "L2":
                if (btnref == 1) {
                    f_log("Button 1 clicked")
                }
                break;
        }
    }
  }
  
  function cust_quizclicked(modref, intref, btnref, fdbck) {
    f_log("Module " + modref + " Interaction " + intref + " button " + btnref + " feedback " + fdbck)
    if (modref == "module03") {
        switch (intref) {
            case "L2":
                if (btnref == 1) {
                    f_log("Button 1 clicked")
                }
                break;
        }
    }
  }
  
  
  
  var mn_frm
  function c_showpopup(){
  mn_frm=_stage.currentFrame()
  _stage.goToLabel('pop1')
  }
  
  function c_hidepopup(){
  _stage.goToFrame(mn_frm)
  }
  
  function C_AddOrder(ref,e,itemId){
  C_CrabOrders.AddOrders(ref,e,itemId);
  }
  function C_RemoveOrder(ref,e,itemId){
  C_CrabOrders.RemoveOrders(ref,e,itemId);
  }
  
  function C_ResetOrder(ref,e){
    C_CrabOrders.ResetOrders(ref,e);
    }
  
  function C_SubmitOrder(){
  C_CrabOrders.SubmitOrder();
  }
  function C_InitOrder(){
  C_CrabOrders.Init();
  }
  
  var C_CrabOrders = (function () {
  var _orders = {
    "S4":{value:0,incrementVal:4,inputId:"F2", minusBtn: "B14"},
    "S3":{value:0,incrementVal:3,inputId:"F3", minusBtn: "B13"},
    "S2":{value:0,incrementVal:2,inputId:"F4", minusBtn: "B12"},
    "S1":{value:0,incrementVal:1,inputId:"F5", minusBtn: "B11"},
    "Total": {value:0},
    "SubmitBtn": "B5",
    "attempts":0
  }
  return {
      Init: function(){
        _orders.attempts = 0;
      },
      AddOrders: function(ref,e,orderItem){
        _orders[orderItem].value = _orders[orderItem].value + _orders[orderItem].incrementVal;
        this.UpdateValues(orderItem);
        this.DisplayTotal();
        _stage[_orders[orderItem].minusBtn].enable();
      },
      RemoveOrders: function(ref,e,orderItem){
        if(_orders[orderItem].value>0){
          _orders[orderItem].value = _orders[orderItem].value - _orders[orderItem].incrementVal;
          this.UpdateValues(orderItem);
          this.DisplayTotal();
          if(_orders[orderItem].value==0){
            _stage[_orders[orderItem].minusBtn].disable();
          }
        }
      },
      UpdateValues: function(orderItem){
        if(_orders[orderItem].value<=0){
          _stage[_orders[orderItem].inputId].setValue("");
        }
        else{
          _stage[_orders[orderItem].inputId].setValue(_orders[orderItem].value)
        }
      },
      DisplayTotal: function(){
        var totalval = _orders["S4"].value + _orders["S3"].value + _orders["S2"].value + _orders["S1"].value;
        if(totalval<=0){
          _stage.F6.setValue("");
          _stage[_orders.SubmitBtn].disable();
  
        }
        else{
          _stage.F6.setValue(totalval);
          _stage[_orders.SubmitBtn].enable();
        }
      },
      SubmitOrder: function(){
        debugger;
        if(_orders.Total.value == 36){
          _stage.feedbackmc.goToLabel("l_correct");
        }
        else{
          if(_orders.attempts==0){
            _stage.feedbackmc.goToLabel("l_incorrect");
            _stage.feedbackmc.B9.visible();
          }
          else if(_orders.attempts>0){
            _stage.feedbackmc.goToLabel("l_showanswer");
          }
        }
        _orders.attempts++;
      },
      ResetOrder: function(){
        debugger;
        _stage[_orders["S4"].inputId].setValue("");
        _stage[_orders["S3"].inputId].setValue("");
        _stage[_orders["S2"].inputId].setValue("");
        _stage[_orders["S1"].inputId].setValue("");
        _stage.F6.setValue("");
      }
  };
  })();
  
  
  function fed(ref) {
  let no_of_attempt = _stage.Q1.attempts;
  if (no_of_attempt > 1) {
    _stage.C1.goToLabel('l_triesexhaust');
  }
  }