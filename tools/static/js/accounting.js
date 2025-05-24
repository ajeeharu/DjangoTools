// 会計用UTIL
let spending_amount_total = 0; // 支出合計
let income_amount_total = 0; // 収入合計
let pagedata_json; // 表示ページ情報
let budgetdata_json; // 各予算情報
const element_tbody = document.querySelector("#AccountingList");

//  Description ： 表示初期化
const InitPage = () => {
  spending_amount_total = 0; // 支出合計
  income_amount_total = 0; // 収入合計
  while (element_tbody.firstChild) {
    element_tbody.removeChild(element_tbody.firstChild);
  }
};
//  Description ： レンダリング
const RenderingPage = (result) => {
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
    // Update用のボタン
    let td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";

    let button_element = document.createElement("button");
    button_element.type = "button";
    button_element.className =
      "window-update-button font-medium text-blue-600 mx-auto";
    button_element.setAttribute("data-number", data.number);

    let href_element = document.createElement("a");
    href_element.href = "#";
    href_element.innerHTML =
      '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">' +
      '<path fill="currentColor" d="m18.988 2.012l3 3L19.701 7.3l-3-3zM8 16h3l7.287-7.287l-3-3L8 13z"/>' +
      '<path fill="currentColor"' +
      'd="M19 19H8.158c-.026 0-.053.01-.079.01c-.033 0-.066-.009-.1-.01H5V5h6.847l2-2H5c-1.103 0-2 .896-2 2v14c0 1.104.897 2 2 2h14a2 2 0 0 0 2-2v-8.668l-2 2z"' +
      "/>" +
      "</svg>";
    button_element.appendChild(href_element);
    td_element.appendChild(button_element);
    tr_element.appendChild(td_element);

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
    // Delete用のボタン
    td_element = document.createElement("td");
    td_element.className = "border-gray-500 border-x border-solid text-center";

    button_element = document.createElement("button");
    button_element.type = "button";
    button_element.className =
      "window-delete-button font-medium text-red-600 mx-auto";
    button_element.setAttribute("data-number", data.number);

    href_element = document.createElement("a");
    href_element.href = "#";
    href_element.innerHTML =
      '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">' +
      '<path fill="currentColor" d="M7 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v2h4a1 1 0 1 1 0 2h-1.069l-.867 12.142A2 2 0 0 1 17.069 22H6.93a2 2 0 0 1-1.995-1.858L4.07 8H3a1 1 0 0 1 0-2h4zm2 2h6V4H9zM6.074 8l.857 12H17.07l.857-12zM10 10a1 1 0 0 1 1 1v6a1 1 0 1 1-2 0v-6a1 1 0 0 1 1-1m4 0a1 1 0 0 1 1 1v6a1 1 0 1 1-2 0v-6a1 1 0 0 1 1-1"/>' +
      "</svg>";
    button_element.appendChild(href_element);
    td_element.appendChild(button_element);
    tr_element.appendChild(td_element);
    // tr（1行）書き込み
    element_tbody.appendChild(tr_element);
  }
};

//  Description ： PageManagerの番号のDBへのUpdate処理(PATCH)
const PageManagerPatchNumber = async (id, number) => {
  try {
    // API経由でData取得
    const CreateEndPoint = "/api/accounting/pagemanager/" + id + "/";
    let response = await fetch(CreateEndPoint, {
      method: "PATCH",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        number: number,
      }),
    });
    let result = await response.json();
  } catch (error) {
    console.error("PATCH API通信エラーが発生しました,error");
  }
};

//  Description ： 収入番号のDBへのUpdate処理(PATCH)
const IncomeRecordPatchNumber = async (id, number) => {
  try {
    // API経由でData取得
    const CreateEndPoint = "/api/accounting/incomerecord/" + id + "/";
    let response = await fetch(CreateEndPoint, {
      method: "PATCH",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        number: number,
      }),
    });
    let result = await response.json();
  } catch (error) {
    console.error("PATCH API通信エラーが発生しました,error");
  }
};

//  Description ： 支出番号のDBへのUpdate処理(PATCH)
const SpendingRecordPatchNumber = async (id, number) => {
  try {
    // API経由でData取得
    const CreateEndPoint = "/api/accounting/spendingrecord/" + id + "/";
    let response = await fetch(CreateEndPoint, {
      method: "PATCH",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        number: number,
      }),
    });
    let result = await response.json();
  } catch (error) {
    console.error("PATCH API通信エラーが発生しました,error");
  }
};

//  Description ： 支出執行済み金額のDBへのUpdate処理(PATCH)
const SpendingRecordPatchCalculateAmount = async (id, amount) => {
  try {
    // API経由でData取得
    const CreateEndPoint = "/api/accounting/spendingrecord/" + id + "/";
    let response = await fetch(CreateEndPoint, {
      method: "PATCH",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        calculate_amount: amount,
      }),
    });
    let result = await response.json();
  } catch (error) {
    console.error("PATCH API通信エラーが発生しました,error");
  }
};

//  Description ： 出納帳、期間よりDBから各予算を抽出
const GetBudgetSpending = async (fiscal_terms, accounting_book) => {
  try {
    // API経由でData取得
    const CreateEndPoint =
      "/api/accounting/subjectspending/?accounting_book=" +
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
    budgetdata_json = result;
  } catch (error) {
    console.error("GET API通信エラーが発生しました,error");
  }
};

//  Description ： PageManagerのシリアル番号を整理する。
//  return ： true(変更有)/false(変更なし)
const CheckPageNumber = async (result) => {
  let retry = false;
  let page_counter = 1;

  for (let i = 0; i < result.length; i++) {
    let data = result[i];
    // PageManagerのSerialNo.がずれていたらReNumber
    if (page_counter != data.number) {
      await PageManagerPatchNumber(data.id, page_counter);
      retry = true;
    }
    page_counter++;
  }
  return retry;
};

//  Description ： 収入番号を整理する。
//  return ： true(変更有)/false(変更なし)
const CheckIncomeNumber = async (result) => {
  let retry = false;
  let income_counter = 1;

  for (let i = 0; i < result.length; i++) {
    let data = result[i];
    // 番号固定でなければ支出番号、収入番号をチェック
    if (data.income_select.value != "支出命令") {
      if (
        income_counter != data.income_record.number &&
        !data.income_record.fixed_number
      ) {
        await IncomeRecordPatchNumber(data.income_record.id, income_counter);
        retry = true;
      }
      if(!data.income_record.fixed_number){
        income_counter++;
      }
    }
  }
  return retry;
};

//  Description ： 支出番号を整理する。
//  return ： true(変更有)/false(変更なし)
const CheckSpendingNumber = async (result) => {
  let retry = false;
  let spending_counter = 1;

  for (let i = 0; i < result.length; i++) {
    let data = result[i];
    if ( data.income_select.value == "支出命令") {
      if (
        spending_counter != data.spending_record.number &&
        !data.spending_record.fixed_number
      ) {
        await SpendingRecordPatchNumber(
          data.spending_record.id,
          spending_counter
        );
        retry = true;
      }
      if (!data.spending_record.fixed_number) {
         spending_counter++;
      }
    }
  }
  return retry;
};

//  Description ： 支出の予算残額を整理する。
const CheckSpendingBudget = async (result) => {
  try {
    await GetBudgetSpending(fiscal_terms_value, accounting_book_value);

    // 予算残額の項目を追加・初期化
    for (let j = 0; j < budgetdata_json.length; j++) {
      budgetdata_json[j].calculate_amount = 0;
    }

    for (let i = 0; i < result.length; i++) {
      let data = result[i];
      if (data.income_select.value == "支出命令") {
        for (let j = 0; j < budgetdata_json.length; j++) {
          if (
            budgetdata_json[j].id == data.spending_record.subject_spending.id
          ) {
            await SpendingRecordPatchCalculateAmount(
              data.spending_record.id,
              budgetdata_json[j].calculate_amount
            );
            budgetdata_json[j].calculate_amount += data.spending_record.amount;
          }
        }
      }
    }
    // レンダリング
    let element_target = document.querySelector("#BudgetTable");
    while (element_target.firstChild) {
      element_target.removeChild(element_target.firstChild);
    }
    for (let j = 0; j < budgetdata_json.length; j += 3) {
      let div_element = document.createElement("div");
      let table_element = document.createElement("table");
      table_element.className = "text-sm text-gray-500";
      let thead_element = document.createElement("thead");
      thead_element.className = "text-sm text-gray-500 bg-gray-100 border-b";
      thead_element.innerHTML =
        '<th scope="col" class="text-center p-2">科　目</th>' +
        '<th scope="col" class="text-center p-2">予算額</th>' +
        '<th scope="col" class="text-center p-2">執行済額</th>' +
        '<th scope="col" class="text-center p-2">予算残額</th>';
      table_element.appendChild(thead_element);

      for (let i = j; i < budgetdata_json.length && i < j + 3; i++) {
        let tr_element = document.createElement("tr");
        tr_element.className = "bg-white border-b hover:bg-gray-50";
        let th_element = document.createElement("th");
        th_element.setAttribute("scope", "row");
        th_element.className =
          "p-2 font-medium text-gray-700 whitespace-nowrap";
        th_element.textContent = budgetdata_json[i].name;
        tr_element.appendChild(th_element);
        let td_element = document.createElement("td");
        td_element.className = "p-2";
        td_element.textContent = budgetdata_json[i].budget.toLocaleString(
          "ja-JP",
          { style: "currency", currency: "JPY" }
        );
        tr_element.appendChild(td_element);
        td_element = document.createElement("td");
        td_element.className = "p-2";
        td_element.textContent = budgetdata_json[
          i
        ].calculate_amount.toLocaleString("ja-JP", {
          style: "currency",
          currency: "JPY",
        });
        tr_element.appendChild(td_element);
        td_element = document.createElement("td");
        td_element.className = "p-2";
        let remaining_amount =
          budgetdata_json[i].budget - budgetdata_json[i].calculate_amount;
        td_element.textContent = remaining_amount.toLocaleString("ja-JP", {
          style: "currency",
          currency: "JPY",
        });
        tr_element.appendChild(td_element);
        table_element.appendChild(tr_element);
      }
      div_element.appendChild(table_element);
      element_target.appendChild(div_element);
    }
  } catch (error) {
    console.error("レンダリング中にエラーが発生しました,error");
  }
};

//  Description ： レンダリング及び変数の設定が終了後にCallBackする関数を設定
let callback_afterRendering = null;
const SetCallBack_afterRendering = (func) => {
  callback_afterRendering = func;
};

//  Description ： 出納帳、期間よりDBからPage情報を取得（番号の整理も行う。）
const PageManagerList = async (fiscal_terms, accounting_book) => {
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
    let retry = await CheckPageNumber(result);
    retry |= await CheckSpendingNumber(result);
    retry |= await CheckIncomeNumber(result);
    if (retry) {
      return await PageManagerList(fiscal_terms_value, accounting_book_value);
    }
    // ここまででページ内の番号や順番は確定済み
    await CheckSpendingBudget(result);
    RenderingPage(result);
    SetTotalAmount();
    pagedata_json = result;
    if (callback_afterRendering != null) {
      callback_afterRendering();
    }
  } catch (error) {
    console.error("GET API通信エラーが発生しました,error");
  }
};

//  Description ： PageManagerのList順番を変更
const PageManagerRenumber = async (result) => {
  await CheckPageNumber(result);
  await CheckSpendingNumber(result);
  await CheckIncomeNumber(result);
  PageManagerList(fiscal_terms_value, accounting_book_value);
};

// Description ； LISTの行替えEvent発生
const onEndEvent = (event) => {
  // console.log("onEnd!!");
  let elements_serial = document.querySelectorAll(".data-serial-number");
  let result = new Array();

  for (i = 0; i < elements_serial.length; i++) {
    result[i] = pagedata_json[elements_serial[i].textContent - 1];
  }
  PageManagerRenumber(result);
};

new Sortable(AccountingList, {
  multiDrag: true, // Enable multi-drag
  selectedClass: "selected", // The class applied to the selected items
  fallbackTolerance: 3, // So that we can select items on mobile
  animation: 150,
  //    onStart: onStartEvent,      // 2-1, ドラッグ開始時
  onEnd: onEndEvent, // 2-2, ドラッグ終了時
  //    onChange: onChangeEvent,    // 2-3, ドラッグ変化時
  //    onSort: onSortEvent,        // 2-4, 並び替え終了時
});

// Warning Message
const element_warning_message = document.querySelector("#warning_message");

// 会計年度と出納帳の選択状況
const element_fiscal_terms = document.querySelector("#select_fiscal_terms");
const element_accounting_book = document.querySelector(
  "#select_accounting_book"
);
const element_income_total = document.querySelector("#income_total");
const element_spendign_total = document.querySelector("#spending_total");

let fiscal_terms_value = 0;
let accounting_book_value = 0;

const SetTotalAmount = () => {
  element_spendign_total.textContent = spending_amount_total.toLocaleString(
    "ja-JP",
    { style: "currency", currency: "JPY" }
  );
  element_income_total.textContent = income_amount_total.toLocaleString(
    "ja-JP",
    { style: "currency", currency: "JPY" }
  );
};

const SetPageListAndWarning = () => {
  if (fiscal_terms_value == 0) {
    element_warning_message.textContent = "会計年度を選択してください！";
    element_warning_message.classList.remove("hidden");
    InitPage();
    SetTotalAmount();
  } else if (accounting_book_value == 0) {
    element_warning_message.textContent = "出納帳を選択してください！";
    element_warning_message.classList.remove("hidden");
    InitPage();
    SetTotalAmount();
  } else {
    element_warning_message.textContent = "";
    element_warning_message.classList.add("hidden");
    PageManagerList(fiscal_terms_value, accounting_book_value);
    // SetTotalAmount(); 非同期のためPageManagerList内で同期待ち合わせ
  }
  // URLを変更
  history.pushState(
    "",
    "",
    "/accounting/index/" + fiscal_terms_value + "/" + accounting_book_value
  );
};

const SetAccountingParameter = (fiscal_terms, accounting_book) => {
  fiscal_terms_value = fiscal_terms;
  accounting_book_value = accounting_book;

  SetSelect(element_fiscal_terms.options, fiscal_terms_value);
  SetSelect(element_accounting_book.options, accounting_book_value);
  SetPageListAndWarning();
  element_fiscal_terms.addEventListener("change", (event) => {
    fiscal_terms_value = event.target.value;
    SetPageListAndWarning();
  });
  element_accounting_book.addEventListener("change", (event) => {
    accounting_book_value = event.target.value;
    SetPageListAndWarning();
  });
};

// モーダル表示前のチェック
const CheckAccountingBook = () => {
  return fiscal_terms_value == 0 || accounting_book_value == 0;
};

// 子Window制御

let child_window;

const element_open_window_incomecreate = document.querySelector(
  "#open-window-income-create"
);
const element_open_window_spendingcreate = document.querySelector(
  "#open-window-spending-create"
);
document.addEventListener("DOMContentLoaded", () => {
  if (child_window && !child_window.closed) {
    child_window.close();
  }
  element_open_window_incomecreate.addEventListener("click", (event) => {
    if (!CheckAccountingBook()) {
      child_window = window.open(
        "/accounting/incomerecord/create/" +
          fiscal_terms_value +
          "/" +
          accounting_book_value +
          "/" +
          (pagedata_json.length + 1),
        "income_create_record",
        "width=896px"
      );
    }
  });
  element_open_window_spendingcreate.addEventListener("click", (event) => {
    if (!CheckAccountingBook()) {
      child_window = window.open(
        "/accounting/spendingrecord/create/" +
          fiscal_terms_value +
          "/" +
          accounting_book_value +
          "/" +
          (pagedata_json.length + 1),
        "spending_create_record",
        "width=896px"
      );
    }
  });
});

// Description: Updateボタン押下時にボタンの情報から支出・収入のUpdate用の子Windowを開く
const windowOpenUpdate = (event) => {
  const page_number =
    event.currentTarget.attributes.getNamedItem("data-number").value;
  let data = pagedata_json[page_number - 1];
  if (data.income_select.value == "支出命令") {
    child_window = window.open(
      "/accounting/spendingrecord/" +
        data.spending_record.id +
        "/update/" +
        fiscal_terms_value +
        "/" +
        accounting_book_value,
      "spending_update_record",
      "width=896px"
    );
  } else {
    child_window = window.open(
      "/accounting/incomerecord/" +
        data.income_record.id +
        "/update/" +
        fiscal_terms_value +
        "/" +
        accounting_book_value,
      "income_update_record",
      "width=896px"
    );
  }
  return true;
};

// Description: レンダリング終了後にUpdateEvent処理を行う。
const SetUpdateEvent = () => {
  const WindowOpenButtons = document.querySelectorAll(".window-update-button");

  //  Window OPENボタン処理
  WindowOpenButtons.forEach((windowbutton) => {
    windowbutton.addEventListener("click", (event) => {
      windowOpenUpdate(event);
    });
  });
};
// Description: Deleteボタン押下時にボタンの情報から支出・収入のUpdate用の子Windowを開く
const windowOpenDelete = (event) => {
  const page_number =
    event.currentTarget.attributes.getNamedItem("data-number").value;
  let data = pagedata_json[page_number - 1];
  if (data.income_select.value == "支出命令") {
    child_window = window.open(
      "/accounting/spendingrecord/" + data.spending_record.id + "/delete",
      "spending_delete_record",
      "width=896px"
    );
  } else {
    child_window = window.open(
      "/accounting/incomerecord/" + data.income_record.id + "/delete",
      "income_delete_record",
      "width=896px"
    );
  }
  return true;
};

// Description: レンダリング終了後にDeleteEvent処理を行う。
const SetDeleteEvent = () => {
  const WindowOpenButtons = document.querySelectorAll(".window-delete-button");

  //  Window OPENボタン処理
  WindowOpenButtons.forEach((windowbutton) => {
    windowbutton.addEventListener("click", (event) => {
      windowOpenDelete(event);
    });
  });
};
// Description：レンダリング終了後CallBackされる関数群
const CallBackFunction_afterRedering = () => {
  SetUpdateEvent();
  SetDeleteEvent();
};
SetCallBack_afterRendering(CallBackFunction_afterRedering);

// Description: データをExcelにexport
const ExportSetting = () => {
  window.location.href =
    "/accounting/export/" + fiscal_terms_value + "/" + accounting_book_value;
};
