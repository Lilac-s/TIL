# JS table



```js
const getInfo = async () => {
    const response = await fetch("/web/src/data.json");
    const data = await response.json()
    return data;
  }
  (async () => {
    dataList = await getInfo()

    const rowCnt = dataList.length;
    const columnCnt = Object.keys(dataList[0]).length;

    //* 테이블 컬럼 헤드 만들기
    let tableHead = "<thead id='gray_column'><tr>"
    for (let head = 0; head < columnCnt; head++) {
        tableHead += `<th>${Object.keys(dataList[0])[head]}</th>`
    }
    tableHead += "</tr></thead>"

    //* 테이블 내용 만들기
    let table = `<table>${tableHead}<tbody>`
    for (let row = 0; row < rowCnt; row++) {
        if (row%2 === 0) {
            table += "<tr>"
        } else if (row%2 === 1) {
            table += "<tr id='gray_column'>"
        }
        for (let key in dataList[row])  {
            table += "<td>";
            table += `${dataList[row][key]}`
            table += '</td>';
        }
        table += '</tr>'
    }
    table += '</tbody></table>'
    //* 영역에 table 넣어주기
    element = document.getElementById('table').innerHTML = table
})()
```

