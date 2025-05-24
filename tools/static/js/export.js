// 会計用UTIL
let spending_amount_total = 0; // 支出合計
let income_amount_total = 0; // 収入合計
let pagedata_json; // 表示ページ情報
let budgetdata_json; // 各予算情報
const element_tbody = document.querySelector("#AccountingList");

//  Description ： 表示初期化
const InitPage = () => {
  while (element_tbody.firstChild) {
    element_tbody.removeChild(element_tbody.firstChild);
  }
};
//  Description ： レンダリング
const RenderingPageforExport = (result) => {
  // 表示を初期化
  InitPage();

  for (let i = 0; i < result.length; i++) {
    let data = result[i];

    let tr_element = document.createElement("tr");
    tr_element.className = "border-gray-500 border-y border-solid";
    let debug_element = document.createElement("td");
    // データ（シリアルNo.）
    debug_element.className =
      "border-gray-500 border-x border-solid text-center data-serial-number hidden";
    debug_element.textContent = data.number;
    tr_element.appendChild(debug_element);

    // 番号固定
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";

    button_element = document.createElement("button");
    button_element.type = "button";
    button_element.className = "font-medium text-gray-500 mx-auto";
    if (
      (data.income_select.value == "支出命令" &&
        data.spending_record.fixed_number) ||
      (data.income_select.value != "支出命令" &&
        data.income_record.fixed_number)
    ) {
      button_element.innerHTML =
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">' +
        '<path fill="currentColor"' +
        'd="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2m0 16H5V5h14zM17.99 9l-1.41-1.42l-6.59 6.59l-2.58-2.57l-1.42 1.41l4 3.99z"' +
        "/>" +
        "</svg>";
    } else {
      button_element.innerHTML =
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">' +
        '<path fill="currentColor" d="M3 21V3h18v18zm2-2h14V5H5zm0 0V5z" />' +
        "</svg>";
    }
    td_element.appendChild(button_element);
    tr_element.appendChild(td_element);
    //月
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";
    let month;
    if (data.income_select.value == "支出命令") {
      td_element.textContent = data.spending_record.date.substring(5, 7);
    } else {
      td_element.textContent = data.income_record.date.substring(5, 7);
    }
    tr_element.appendChild(td_element);

    //日
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";
    if (data.income_select.value == "支出命令") {
      td_element.textContent = data.spending_record.date.substring(8, 10);
    } else {
      td_element.textContent = data.income_record.date.substring(8, 10);
    }
    tr_element.appendChild(td_element);
    //項
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";
    if (data.income_select.value == "支出命令") {
      td_element.textContent = data.spending_record.subject_spending.acronym;
    } else {
      td_element.textContent = data.income_record.subject_income.acronym;
    }
    tr_element.appendChild(td_element);
    //節
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";
    if (data.income_select.value == "支出命令") {
      td_element.textContent = data.spending_record.section_spending.acronym;
    } else {
      td_element.textContent = data.income_record.section_income.acronym;
    }
    tr_element.appendChild(td_element);
    //債権者・納入者
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";
    if (data.income_select.value == "支出命令") {
      td_element.textContent = data.spending_record.creditor.name;
    } else {
      td_element.textContent = data.income_record.supplier.name;
    }
    tr_element.appendChild(td_element);
    //概要
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";
    if (data.income_select.value == "支出命令") {
      td_element.textContent = data.spending_record.description;
    } else {
      td_element.textContent = data.income_record.description;
    }
    tr_element.appendChild(td_element);
    //収入番号
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";
    if (data.income_select.value == "支出命令") {
    } else {
      td_element.textContent = data.income_record.number;
    }
    tr_element.appendChild(td_element);
    //支出番号
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";
    if (data.income_select.value == "支出命令") {
      td_element.textContent = data.spending_record.number;
    } else {
    }
    tr_element.appendChild(td_element);
    //収入金額
    td_element = document.createElement("td");
    td_element.className =
      "border-gray-500 border-x border-solid text-right pr-1 text-xs";
    if (data.income_select.value == "支出命令") {
    } else {
      td_element.textContent = data.income_record.amount.toLocaleString(
        "ja-JP",
        { style: "currency", currency: "JPY" }
      );
      income_amount_total += data.income_record.amount;
    }
    tr_element.appendChild(td_element);
    //支出金額
    td_element = document.createElement("td");
    td_element.className =
      "border-gray-500 border-x border-solid text-right pr-1 text-xs";
    if (data.income_select.value == "支出命令") {
      td_element.textContent = data.spending_record.amount.toLocaleString(
        "ja-JP",
        { style: "currency", currency: "JPY" }
      );
      spending_amount_total += data.spending_record.amount;
    } else {
    }
    tr_element.appendChild(td_element);
    //差引残高
    td_element = document.createElement("td");
    td_element.className =
      "border-gray-500 border-x border-solid text-right pr-1 text-xs";
    td_element.textContent = (
      income_amount_total - spending_amount_total
    ).toLocaleString("ja-JP", { style: "currency", currency: "JPY" });
    tr_element.appendChild(td_element);
    //見積もり
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";
    if (data.income_select.value == "支出命令") {
      if (data.spending_record.estimate != null) {
        button_element = document.createElement("button");
        button_element.type = "button";
        button_element.className = "font-medium text-gray-500 mx-auto";
        href_element = document.createElement("a");
        href_element.href = data.spending_record.estimate;
        href_element.innerHTML =
          '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">' +
          '<path fill="currentColor" d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zm4 18H6V4h7v5h5z"/>' +
          "</svg>";
        button_element.appendChild(href_element);
        td_element.appendChild(button_element);
      }
    } else {
      if (data.income_record.notice1 != null) {
        button_element = document.createElement("button");
        button_element.type = "button";
        button_element.className = "font-medium text-gray-500 mx-auto";
        href_element = document.createElement("a");
        href_element.href = data.income_record.notice1;
        href_element.innerHTML =
          '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">' +
          '<path fill="currentColor" d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zm4 18H6V4h7v5h5z"/>' +
          "</svg>";
        button_element.appendChild(href_element);
        td_element.appendChild(button_element);
      }
    }
    tr_element.appendChild(td_element);
    //領収
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";
    if (data.income_select.value == "支出命令") {
      if (data.spending_record.receipt != null) {
        button_element = document.createElement("button");
        button_element.type = "button";
        button_element.className = "font-medium text-gray-500 mx-auto";
        href_element = document.createElement("a");
        href_element.href = data.spending_record.receipt;
        href_element.innerHTML =
          '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">' +
          '<path fill="currentColor" d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zm4 18H6V4h7v5h5z"/>' +
          "</svg>";
        button_element.appendChild(href_element);
        td_element.appendChild(button_element);
      }
    } else {
      if (data.income_record.notice2 != null) {
        button_element = document.createElement("button");
        button_element.type = "button";
        button_element.className = "font-medium text-gray-500 mx-auto";
        href_element = document.createElement("a");
        href_element.href = data.income_record.notice2;
        href_element.innerHTML =
          '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">' +
          '<path fill="currentColor" d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zm4 18H6V4h7v5h5z"/>' +
          "</svg>";
        button_element.appendChild(href_element);
        td_element.appendChild(button_element);
      }
    }
    tr_element.appendChild(td_element);
    // tr（1行）書き込み
    element_tbody.appendChild(tr_element);
  }
};

// Description: データをExcelにexport
const DownloadExcel = async () => {
  try {
    // Djangoへデータを送信してExcelをダウンロードする。
    const CreateEndPoint = "/accounting/downloadexcel";
    let response = await fetch(CreateEndPoint, {
      method: "POST",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
      body: JSON.stringify(pagedata_json),
    });
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "sample.xlsx";
    a.click();
  } catch (error) {
    console.error("GET API通信エラーが発生しました,error");
  }
};

//  Description ： 出納帳、期間よりDBからPage情報を取得（番号の整理も行う。）
const PageManagerListforExport = async (fiscal_terms, accounting_book) => {
  try {
    // API経由でData取得
    const CreateEndPoint =
      "/api/accounting/pagemanager/?accounting_book=" +
      accounting_book +
      "&fiscal_terms=" +
      fiscal_terms;
    let response = await fetch(CreateEndPoint, {
      method: "GET",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
    });
    let result = await response.json(); // 読み込むのはJSON部分（ヘッダー等は削除）
    // ここまででページ内の番号や順番は確定済み
    RenderingPageforExport(result);
  } catch (error) {
    console.error("GET API通信エラーが発生しました,error");
  }
};

//
const ExportAccountingParameter = (fiscal_terms, accounting_book) => {
  fiscal_terms_value = fiscal_terms;
  accounting_book_value = accounting_book;

  PageManagerListforExport(fiscal_terms_value, accounting_book_value);
};
