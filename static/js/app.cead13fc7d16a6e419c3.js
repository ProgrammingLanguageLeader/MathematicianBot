webpackJsonp([1],{"72AV":function(t,e){},"9M+g":function(t,e){},BKXk:function(t,e){},"GbO+":function(t,e){},Jmt5:function(t,e){},NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=n("7+uW"),a={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("b-navbar",{attrs:{type:"dark",variant:"info",toggleable:"sm"}},[n("b-container",[n("b-navbar-brand",{attrs:{href:"#"}},[t._v("\n        Mathematician Bot\n      ")]),t._v(" "),n("b-navbar-toggle",{attrs:{target:"nav-collapse"}}),t._v(" "),n("b-collapse",{attrs:{id:"nav-collapse","is-nav":""}},[n("b-navbar-nav",[n("b-nav-item",{attrs:{to:"/"}},[t._v("\n            Web\n          ")]),t._v(" "),n("b-nav-item",{attrs:{href:"https://t.me/clever_mathematician_bot"}},[t._v("\n            Telegram\n          ")]),t._v(" "),n("b-nav-item",{attrs:{href:"#",disabled:""}},[t._v("\n            VK\n          ")])],1)],1)],1)],1),t._v(" "),n("router-view")],1)},staticRenderFns:[]};var i=n("VU/8")({name:"App"},a,!1,function(t){n("BKXk")},null,null).exports,o=n("/ocq"),s={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("b-container",{staticClass:"pt-4"},[n("h3",[t._v("Choose an option to start")]),t._v(" "),n("b-list-group",[n("b-list-group-item",{attrs:{to:"/integral"}},[t._v("\n      Integral\n    ")]),t._v(" "),n("b-list-group-item",{attrs:{to:"/derivative"}},[t._v("\n      Derivative\n    ")]),t._v(" "),n("b-list-group-item",{attrs:{to:"/limit"}},[t._v("\n      Limit\n    ")]),t._v(" "),n("b-list-group-item",{attrs:{to:"/sum"}},[t._v("\n      Sum\n    ")]),t._v(" "),n("b-list-group-item",{attrs:{to:"/plot"}},[t._v("\n      Plot\n    ")]),t._v(" "),n("b-list-group-item",{attrs:{to:"/equation"}},[t._v("\n      Equation\n    ")]),t._v(" "),n("b-list-group-item",{attrs:{to:"/extrema"}},[t._v("\n      Extrema\n    ")]),t._v(" "),n("b-list-group-item",{attrs:{to:"/taylor-series"}},[t._v("\n      Taylor series\n    ")]),t._v(" "),n("b-list-group-item",{attrs:{to:"/manual-query"}},[t._v("\n      Manual query\n    ")])],1)],1)},staticRenderFns:[]};var l=n("VU/8")({name:"Home"},s,!1,function(t){n("72AV")},"data-v-536e8d5e",null).exports,u={render:function(){var t=this.$createElement,e=this._self._c||t;return e("b-container",{staticClass:"pt-4"},[e("h1",[this._v("Page not found")])])},staticRenderFns:[]};var c=n("VU/8")({name:"NotFound"},u,!1,function(t){n("OMk1")},"data-v-0db12e74",null).exports,p=n("Xxa5"),b=n.n(p),m=n("exGp"),v=n.n(m),d={methods:{onSubmit:function(t){var e=this;return v()(b.a.mark(function n(){var r,a,i,o,s;return b.a.wrap(function(n){for(;;)switch(n.prev=n.next){case 0:return t.preventDefault(),r=new URL("https://mathematician-bot.herokuapp.com/api"+"/simple"),a="integrate "+e.integratingFunction+" d"+e.independentVariable,e.fromNumber.length>0&&(a+=" from "+e.fromNumber),e.toNumber.length>0&&(a+=" to "+e.toNumber),i={request:a},r.search=new URLSearchParams(i),e.fetching=!0,n.next=11,fetch(r);case 11:if(200===(o=n.sent).status){n.next=17;break}e.error=!0,e.answer=null,n.next=25;break;case 17:return e.error=!1,(s=new FileReader).onload=function(t){e.answer=t.target.result},n.t0=s,n.next=23,o.blob();case 23:n.t1=n.sent,n.t0.readAsDataURL.call(n.t0,n.t1);case 25:e.fetching=!1;case 26:case"end":return n.stop()}},n,e)}))()}},data:function(){return{integratingFunction:"x^2",independentVariable:"x",fromNumber:"",toNumber:"",answer:null,fetching:!1,error:!1}}},f={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("b-container",{staticClass:"pt-4"},[n("b-form",{on:{submit:t.onSubmit}},[n("b-form-group",{staticClass:"pt-2",attrs:{label:"Enter the following fields to calculate integral"}},[n("b-input-group",{attrs:{prepend:"function"}},[n("b-input",{attrs:{id:"integrating-function",required:"",placeholder:"Enter the function"},model:{value:t.integratingFunction,callback:function(e){t.integratingFunction=e},expression:"integratingFunction"}})],1),t._v(" "),n("b-input-group",{staticClass:"pt-1",attrs:{prepend:"differential: "}},[n("b-input",{attrs:{required:"",placeholder:"Independent variable"},model:{value:t.independentVariable,callback:function(e){t.independentVariable=e},expression:"independentVariable"}})],1),t._v(" "),n("b-input-group",{staticClass:"pt-1",attrs:{prepend:"from"}},[n("b-input",{attrs:{placeholder:"optional"},model:{value:t.fromNumber,callback:function(e){t.fromNumber=e},expression:"fromNumber"}})],1),t._v(" "),n("b-input-group",{staticClass:"pt-1",attrs:{prepend:"to"}},[n("b-input",{attrs:{placeholder:"optional"},model:{value:t.toNumber,callback:function(e){t.toNumber=e},expression:"toNumber"}})],1)],1),t._v(" "),n("b-row",{attrs:{"align-h":"center"}},[n("b-col",{attrs:{md:"6",sm:"12"}},[n("b-button",{attrs:{block:"",type:"submit",variant:"primary"}},[t._v("\n          Submit\n        ")])],1)],1)],1),t._v(" "),t.fetching?n("b-row",{staticClass:"pt-4",attrs:{"align-h":"center"}},[n("b-spinner")],1):t.answer?n("b-container",{staticClass:"mt-2 mb-2"},[n("b-row",{attrs:{"align-h":"center"}},[n("h4",[t._v("Answer")])]),t._v(" "),n("b-row",{attrs:{"align-h":"center"}},[n("b-img",{attrs:{id:"answer-img",src:t.answer}})],1)],1):t.error?n("b-row",{staticClass:"p-2",attrs:{"align-h":"center"}},[t._v("\n    Something went wrong...\n  ")]):t._e()],1)},staticRenderFns:[]};var g=n("VU/8")(d,f,!1,function(t){n("GbO+")},"data-v-3dc70918",null).exports;r.a.use(o.a);var _=new o.a({routes:[{path:"/",name:"Hello",component:l},{path:"/integral",name:"Integral",component:g},{path:"*",name:"Not found",component:c}]});_.beforeEach(function(t,e,n){document.title=t.name,n()});var h=_,w=n("e6fC"),x=n.n(w);n("Jmt5"),n("9M+g");r.a.config.productionTip=!1,r.a.use(x.a),new r.a({el:"#app",router:h,components:{App:i},template:"<App/>"})},OMk1:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.cead13fc7d16a6e419c3.js.map