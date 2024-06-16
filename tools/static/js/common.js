
// Restful API用	COOKIEからCSRFTOKENの値を取得
const getCookie = (name)=> {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      // クッキー名からCSRFトークンを探す
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// モーダル関ライブラリー

let createCallback;
let updateCallback;
let deleteCallback;

const SetCallback = ( func_create=null, func_update=null, func_delete=null ) => {
  createCallback = func_create;
  updateCallback = func_update;
  deleteCallback = func_delete;
}

const modalOpen =(event)=> {
  const target = event.currentTarget.attributes.getNamedItem("data-modal-target").value;
  const modal = document.querySelector(target);
  modal.classList.add("flex");
  modal.classList.remove("hidden");
  const id = event.currentTarget.attributes.getNamedItem("data-modal-id").value;

  if (target == "#create-modal" && createCallback != null) {
    createCallback(id);
  }
  if (target == "#update-modal" && updateCallback != null) {
    updateCallback(id);
  }
  if (target == "#delete-modal" && deleteCallback != null) {
    deleteCallback(id);
  }
};

const modalClose =(event)=>{
  const target = event.currentTarget.attributes.getNamedItem("data-modal-target").value;
  const modal = document.querySelector(target);
  modal.classList.add("hidden");
  modal.classList.remove("flex");
};

document.addEventListener("DOMContentLoaded", () => {
  const modalOpenButtons = document.querySelectorAll(".modal-open-button");
  const modalCloseButtons = document.querySelectorAll(".modal-close-button");

  //  モーダルOPENボタン処理
  modalOpenButtons.forEach((modalbutton) => {
    modalbutton.addEventListener("click", (event) => {
      modalOpen(event);
    });
  });
  //  モーダルCLOSEボタン処理
  modalCloseButtons.forEach((modalbutton) => {
    modalbutton.addEventListener("click", (event) => {
      modalClose(event);
    });
  });
});

// ドロップダウンメニュー関連ライブラり

document.addEventListener("DOMContentLoaded", () => {
  const dropDownButtons = document.querySelectorAll(".dropdownbutton");
  const dropDownMenus = document.querySelectorAll(".dropdownmenu");
  // const toggleArrows = document.querySelectorAll("dropdownarrow");

  // Toggle dropdown open/close when dropdown button is clicked
  dropDownButtons.forEach((dropbutton) => {
    dropbutton.addEventListener("click", (event) => {
      event.stopPropagation();
      event.currentTarget.lastElementChild.classList.toggle("arrow");    // SVGを取得
      const target = event.currentTarget.attributes.getNamedItem("data-dropdown-toggle").value;
      const menu = document.getElementById(target);
      // button位置からmenu位置を設定
      const rect = dropbutton.getBoundingClientRect();
      menu.style.top = rect.bottom + "px";
      menu.style.left = rect.left + "px";
      menu.classList.toggle("hidden");
      menu.classList.toggle("block");
    });
  });
  // Close dropdown when dom element is clicked
  document.documentElement.addEventListener("click",  () => {
    dropDownMenus.forEach((dropmenu) => {
      if (dropmenu.classList.contains("block")) {
        dropmenu.classList.toggle("hidden");
        dropmenu.classList.toggle("block");
        dropDownButtons.forEach((dropbutton) => {
          let target = dropbutton.attributes.getNamedItem("data-dropdown-toggle").value;
          if( dropmenu.id == target )
          {
            dropbutton.lastElementChild.classList.toggle("arrow"); // SVGを取得
          }
        });
      }
    });
  });
});