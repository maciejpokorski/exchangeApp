(function(){"use strict";var e={6324:function(e,n,t){var a=t(9242),r=t(3396);const c={class:"container mt-5"},s={class:"row pb-5"},i={class:"col"},o=["disabled"],l={class:"row"},d={class:"col d-md-flex align-items-center"},u={class:"flex-fill"},g={class:"row"},h={class:"col-md-12"};function p(e,n,t,a,p,f){const b=(0,r.up)("Datepicker"),y=(0,r.up)("ExchangeRatesInline"),w=(0,r.up)("ExchangeRatesTable"),m=(0,r.up)("CurrencyList");return(0,r.wg)(),(0,r.iD)("div",c,[(0,r._)("div",s,[(0,r._)("div",i,[(0,r._)("button",{type:"button",class:"btn btn-primary",disabled:p.isLoading,onClick:n[0]||(n[0]=e=>f.reloadTable())}," Reload data ",8,o)])]),(0,r._)("div",l,[(0,r._)("div",d,[(0,r._)("div",null,[(0,r.Wm)(b,{modelValue:p.date,"onUpdate:modelValue":[n[1]||(n[1]=e=>p.date=e),f.fetchData],clearable:!1,"enable-time-picker":!1,"max-date":new Date},null,8,["modelValue","onUpdate:modelValue","max-date"])]),(0,r._)("div",u,[(0,r.Wm)(y,{exchangeRate:p.exchangeRate,isLoading:p.isLoading},null,8,["exchangeRate","isLoading"])])]),(0,r._)("div",null,[(0,r.Wm)(w,{exchangeRates:p.exchangeRates,isLoading:p.isLoading},null,8,["exchangeRates","isLoading"])])]),(0,r._)("div",g,[(0,r._)("div",h,[(0,r.Wm)(m,{onUpdateCurrency:f.updateCurrencyStatus},null,8,["onUpdateCurrency"])])])])}var f=t(7139);const b={class:"px-md-3 ps-1 mt-md-0 mt-3"},y={key:0,class:"d-inline-flex"},w=(0,r._)("span",{class:"list-item pe-3"},"Loading...",-1),m=[w],v={key:1,class:"row"};function x(e,n,t,a,c,s){return(0,r.wg)(),(0,r.iD)("div",null,[(0,r._)("div",b,[t.isLoading?((0,r.wg)(),(0,r.iD)("div",y,m)):((0,r.wg)(),(0,r.iD)("div",v,[((0,r.wg)(!0),(0,r.iD)(r.HY,null,(0,r.Ko)(t.exchangeRate,((e,n)=>((0,r.wg)(),(0,r.iD)("span",{key:n,class:"col-md-3 col-lg-2 col-6 py-2 list-item pe-md-3 pe-1"},(0,f.zw)(n)+": "+(0,f.zw)(e),1)))),128))]))])])}var _={props:{exchangeRate:Object,isLoading:Boolean}},D=t(89);const k=(0,D.Z)(_,[["render",x]]);var C=k;const L={class:"table-responsive"},R={key:0,class:"d-inline-flex"},O=(0,r._)("span",{class:"list-item pe-3 my-4"},"Loading...",-1),S=[O],E={key:1,class:"table table-responsive table-striped mt-4"};function j(e,n,t,a,c,s){return(0,r.wg)(),(0,r.iD)("div",L,[t.isLoading?((0,r.wg)(),(0,r.iD)("div",R,S)):((0,r.wg)(),(0,r.iD)("table",E,[(0,r._)("thead",null,[(0,r._)("tr",null,[((0,r.wg)(!0),(0,r.iD)(r.HY,null,(0,r.Ko)(t.exchangeRates[0],((e,n)=>((0,r.wg)(),(0,r.iD)("th",{key:e},(0,f.zw)(n),1)))),128))])]),(0,r._)("tbody",null,[((0,r.wg)(!0),(0,r.iD)(r.HY,null,(0,r.Ko)(t.exchangeRates,(e=>((0,r.wg)(),(0,r.iD)("tr",{key:e},[((0,r.wg)(!0),(0,r.iD)(r.HY,null,(0,r.Ko)(e,((e,n)=>((0,r.wg)(),(0,r.iD)("td",{key:n},(0,f.zw)(e),1)))),128))])))),128))])]))])}var T={props:{exchangeRates:Array,isLoading:Boolean}};const z=(0,D.Z)(T,[["render",j]]);var H=z;const I={key:0,class:"accordion",id:"accordionExample"},Z={class:"accordion-item"},K=(0,r._)("h2",{class:"accordion-header",id:"headingOne"},[(0,r._)("button",{class:"accordion-button collapsed",type:"button","data-bs-toggle":"collapse","data-bs-target":"#collapseOne","aria-expanded":"true","aria-controls":"collapseOne"}," Configure currencies ")],-1),U={id:"collapseOne",class:"accordion-collapse collapse","aria-labelledby":"headingOne","data-bs-parent":"#accordionExample"},V={class:"accordion-body"},Y=(0,r._)("h1",null,"Currency List",-1),$={class:"container"},P={class:"d-flex flex-row row"};function W(e,n,t,c,s,i){const o=(0,r.up)("CurrencyItem");return s.currencies&&s.currencies.length>0?((0,r.wg)(),(0,r.iD)("div",I,[(0,r._)("div",Z,[K,(0,r._)("div",U,[(0,r._)("div",V,[Y,(0,r.wy)((0,r._)("input",{"onUpdate:modelValue":n[0]||(n[0]=e=>s.search=e),class:"form-control mb-3",placeholder:"Search currencies"},null,512),[[a.nr,s.search]]),(0,r._)("div",$,[(0,r._)("div",P,[((0,r.wg)(!0),(0,r.iD)(r.HY,null,(0,r.Ko)(i.filteredCurrencies,(e=>((0,r.wg)(),(0,r.j4)(o,{key:e.id,currency:e,onToggleStatus:i.updateCurrencyStatus},null,8,["currency","onToggleStatus"])))),128))])])])])])])):(0,r.kq)("",!0)}const A={class:"p-2 col-sm-2 col-6 border"},B={class:"card-body"},q={class:"card-title"};function F(e,n,t,a,c,s){return(0,r.wg)(),(0,r.iD)("div",A,[(0,r._)("div",B,[(0,r._)("h5",q,(0,f.zw)(t.currency.code),1),(0,r._)("p",{class:(0,f.C_)({"text-success":t.currency.enabled,"text-danger":!t.currency.enabled})}," Status: "+(0,f.zw)(t.currency.enabled?"Enabled":"Disabled"),3),(0,r._)("button",{onClick:n[0]||(n[0]=(...e)=>s.toggleStatus&&s.toggleStatus(...e)),class:"btn btn-primary"},(0,f.zw)(t.currency.enabled?"Disable":"Enable"),1)])])}var G={props:{currency:Object},methods:{toggleStatus(){this.$emit("toggle-status",this.currency)}}};const M=(0,D.Z)(G,[["render",F]]);var N=M;async function J(e,n="GET"){const t="http://localhost:8000/",a=await fetch(t+e,{method:n});if(!a.ok)throw new Error("Network response was not ok");return await a.json()}async function Q(e){const n=`fetch_remote_data/${e.toISOString().slice(0,10)}`;return J(n)}async function X(){const e="fetch_local_data/";return J(e)}async function ee(){const e="get_currencies/";return J(e)}async function ne(e){e.enabled=!e.enabled;const n=`update_currency/${e.id}?enabled=${e.enabled}`;try{return J(n,"PATCH")}catch(t){throw e.enabled=!e.enabled,t}}var te={components:{CurrencyItem:N},data(){return{currencies:[],search:""}},mounted(){this.fetchData()},computed:{filteredCurrencies(){return this.currencies?this.currencies.filter((e=>e.code.toLowerCase().includes(this.search.toLowerCase()))):[]}},methods:{async fetchData(){return ee().then((e=>{this.currencies=e}))},updateCurrencyStatus(e){const n=this.currencies.findIndex((n=>n.id===e.id));-1!==n&&(this.currencies[n].enabled=e.enabled,this.$emit("update-currency",e))}}};const ae=(0,D.Z)(te,[["render",W]]);var re=ae,ce=t(393),se={name:"App",components:{ExchangeRatesInline:C,ExchangeRatesTable:H,CurrencyList:re,Datepicker:ce.Z},data(){return{date:null,exchangeRate:null,exchangeRates:[],isLoading:!0}},async mounted(){this.date=new Date,await this.fetchData()},methods:{async fetchData(){this.isLoading=!0,this.exchangeRate=await Q(this.date),this.isLoading=!1},async reloadTable(){this.fetchData(),this.exchangeRates=[],this.exchangeRates=await X()},async updateCurrencyStatus(e){await ne(e)}}};const ie=(0,D.Z)(se,[["render",p]]);var oe=ie;t(3455);const le=(0,a.ri)(oe);le.config.errorHandler=function(e){console.error(e),alert("Sorry, something went wrong. Please try again later. Error details in the console.")},le.mount("#app")}},n={};function t(a){var r=n[a];if(void 0!==r)return r.exports;var c=n[a]={exports:{}};return e[a].call(c.exports,c,c.exports,t),c.exports}t.m=e,function(){var e=[];t.O=function(n,a,r,c){if(!a){var s=1/0;for(d=0;d<e.length;d++){a=e[d][0],r=e[d][1],c=e[d][2];for(var i=!0,o=0;o<a.length;o++)(!1&c||s>=c)&&Object.keys(t.O).every((function(e){return t.O[e](a[o])}))?a.splice(o--,1):(i=!1,c<s&&(s=c));if(i){e.splice(d--,1);var l=r();void 0!==l&&(n=l)}}return n}c=c||0;for(var d=e.length;d>0&&e[d-1][2]>c;d--)e[d]=e[d-1];e[d]=[a,r,c]}}(),function(){t.n=function(e){var n=e&&e.__esModule?function(){return e["default"]}:function(){return e};return t.d(n,{a:n}),n}}(),function(){t.d=function(e,n){for(var a in n)t.o(n,a)&&!t.o(e,a)&&Object.defineProperty(e,a,{enumerable:!0,get:n[a]})}}(),function(){t.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){t.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)}}(),function(){var e={143:0};t.O.j=function(n){return 0===e[n]};var n=function(n,a){var r,c,s=a[0],i=a[1],o=a[2],l=0;if(s.some((function(n){return 0!==e[n]}))){for(r in i)t.o(i,r)&&(t.m[r]=i[r]);if(o)var d=o(t)}for(n&&n(a);l<s.length;l++)c=s[l],t.o(e,c)&&e[c]&&e[c][0](),e[c]=0;return t.O(d)},a=self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[];a.forEach(n.bind(null,0)),a.push=n.bind(null,a.push.bind(a))}();var a=t.O(void 0,[998],(function(){return t(6324)}));a=t.O(a)})();
//# sourceMappingURL=app.3ad04864.js.map