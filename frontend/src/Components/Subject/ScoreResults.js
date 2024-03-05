import { Link } from "react-router-dom";
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { variables } from "../../Variables";
import Papa from "papaparse";
import Cookies from "js-cookie";
import Swal from 'sweetalert2'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCircleCheck } from "@fortawesome/free-solid-svg-icons";
function AppScoreResults() {
    const { id } = useParams();

    // const [data, setdata] = useState([]);
    const [ExamNo, setExamNo] = useState('');
    const [ExamNoShow, setExamNoShow] = useState('');
    const [subid, setsubid] = useState('');
    const [subjectname, setsubjectname] = useState('');

    const [csvData, setcsvData] = useState([]);
    const [link_result, setlink_result] = useState([]);
    
    const [TextError, setTextError] = useState('');


    const [Start, setStart] = useState(0);
    const [StartError, setStartError] = useState(0);

    const [showscores, setshowscores] = useState(false);
    const [sendemail, setsendemail] = useState(null);

    const handleshowscores = () => {
        if(showscores === false){
            Swal.fire({
                title: ``,
                text: `คุณต้องแสดงข้อมูลการสอบของนักศึกษาใช่หรือไม่ `,
                icon: "question",
                showCancelButton: true,
                confirmButtonColor:"#341699",
                confirmButtonText: "ยืนยัน",
                cancelButtonText:"ยกเลิก"
            }).then(async (result) => {
                if(result.isConfirmed){
                    const response = await fetch(variables.API_URL + "exam/update/"+id+"/", {
                        method: "PUT",
                        headers: {
                            'Accept': 'application/json, text/plain',
                            'Content-Type': 'application/json;charset=UTF-8'
                        },
                        body: JSON.stringify({
                            showscores:1,
                            userid : Cookies.get('userid')
                        }),
                    });
                    Swal.fire({
                        title: ``,
                        text: `ผู้ใช้งานที่มีอีเมล USER ตรงกับอีเมลที่มีในการสอบจะสามารถมองเห็นข้อมูลการสอบชองตนเองได้`,
                        icon: "success",
                        showCancelButton: false,
                        confirmButtonColor:"#341699",
                        confirmButtonText: "ยืนยัน",
                        cancelButtonText:"ยกเลิก"
                    }).then(async (result) => {
                        setshowscores(!showscores);
                        if(result.isConfirmed){
                            
                        }
                    })
                }
            })
        }else{
            Swal.fire({
                title: ``,
                text: `คุณต้องยกเลิกการแสดงข้อมูลการสอบใช่หรือไม่ `,
                icon: "question",
                showCancelButton: true,
                confirmButtonColor:"#341699",
                confirmButtonText: "ยืนยัน",
                cancelButtonText:"ยกเลิก"
            }).then(async (result) => {
                if(result.isConfirmed){
                    const response = await fetch(variables.API_URL + "exam/update/"+id+"/", {
                        method: "PUT",
                        headers: {
                            'Accept': 'application/json, text/plain',
                            'Content-Type': 'application/json;charset=UTF-8'
                        },
                        body: JSON.stringify({
                            showscores: null,
                            userid : Cookies.get('userid')
                        }),
                    });
                    setshowscores(!showscores);
                }
            })
        }
    };
    async function handlesendemail(e) {
        if(sendemail === null){
            Swal.fire({
                title: ``,
                text: `คุณต้องส่งข้อมูลการสอบไปยังอีเมลของนักศึกษาใช่หรือไม่`,
                icon: "question",
                showCancelButton: true,
                confirmButtonColor:"#341699",
                confirmButtonText: "ยืนยัน",
                cancelButtonText:"ยกเลิก"
            }).then(async (result) => {
                console.log(result)
                if(result.isConfirmed){
                    const response = await fetch(variables.API_URL + "exam/update/"+id+"/", {
                        method: "PUT",
                        headers: {
                            'Accept': 'application/json, text/plain',
                            'Content-Type': 'application/json;charset=UTF-8'
                        },
                        body: JSON.stringify({
                            sendemail:1,
                            userid : Cookies.get('userid')
                        }),
                    });
                    fetchDataExaminfo()
                }
            })
        }else{
            Swal.fire({
                title: ``,
                text: `คุณเคยส่งรายละเอียดการสอบไปแล้ว คุณต้องส่งข้อมูลการสอบไปยังอีเมลของนักศึกษาอีกครั้งใช่หรือไม่  `,
                icon: "question",
                showCancelButton: true,
                confirmButtonColor:"#341699",
                confirmButtonText: "ยืนยัน",
                cancelButtonText:"ยกเลิก"
            }).then(async (result) => {
                if(result.isConfirmed){
                    const response = await fetch(variables.API_URL + "exam/update/"+id+"/", {
                        method: "PUT",
                        headers: {
                            'Accept': 'application/json, text/plain',
                            'Content-Type': 'application/json;charset=UTF-8'
                        },
                        body: JSON.stringify({
                            sendemail:1,
                            userid : Cookies.get('userid')
                        }),
                    });
                }
            })
        }
    };
    
    const fetchDataExaminfo = async () => {
        try{
            const response = await fetch(variables.API_URL + "exam/detail/" + id + "/", {
                method: "GET",
                headers: {
                    'Accept': 'application/json, text/plain',
                    'Content-Type': 'application/json;charset=UTF-8'
                },
            });
            const result = await response.json();
    
            if (result.err !== undefined) {
                setStartError(1);
            } else {
                console.log(result)
                setExamNo(result.examno);
                setExamNoShow(result.examid);
                setsubid(result.subid);
                setlink_result(result.result_csv_path)
                const csvResponse = await fetch(result.result_csv_path);
                const csvText = await csvResponse.text();

                parseCSVData(csvText);
                const statu_showscores = result.showscores
                if(statu_showscores === null){
                    setshowscores(false)
                }else{
                    setshowscores(true)
                }
                const statu_sendemail = result.sendemail
                if(statu_sendemail === null){
                    setsendemail(null)
                }else{
                    setsendemail(true)
                }
                
            }
            const subjectResponse = await fetch(variables.API_URL + "subject/detail/" + result.subid + "/", {
                method: "GET",
                headers: {
                    'Accept': 'application/json, text/plain',
                    'Content-Type': 'application/json;charset=UTF-8'
                },
            });
            const subjectResult = await subjectResponse.json();
            if (subjectResult.err !== undefined) {
                setStartError(1);
            }else{
                setsubjectname(subjectResult.subjectname);
            }
        } catch (err) {
            setStartError(1);
        }
    };

    useEffect(() => {
        if (Start === 0) {
            fetchDataExaminfo();
            setStart(1);
            setTimeout(function() {
                setStartError(2)
            }, 800);
        }
    }, [Start]); 

    const parseCSVData = (text) => {
        Papa.parse(text, {
            header: true, 
            dynamicTyping: true,
            skipEmptyLines: true,
            complete: function (result) {
                console.log('Parsed CSV data:', result.data);
                setcsvData(result.data);
            },
        });
    };

    const handleDownload = () => {
        const filePath = link_result;
        const link = document.createElement('a');
        link.href = process.env.PUBLIC_URL + filePath;
        link.download = 'result_student_list.csv';
        link.click();
    };
    return (
        <div className='content'>
            <main>
                <div className='box-content'>
                    {StartError === 0 || StartError === 1 ? 
                        StartError === 0 ? 
                            <div className='box-content-view'>
                                <div className='bx-topic light '>
                                    <div className='skeleton-loading'>
                                        <div className='skeleton-loading-topic'></div>
                                    </div> 
                                </div>
                                <div className='bx-details light '>
                                    <div className='skeleton-loading'>
                                        <div className='skeleton-loading-content'></div>
                                    </div> 
                                </div>
                            </div>
                        :
                            <div className='box-content-view'>
                                <div className='bx-topic light'>เกิดข้อผิดพลาดกรุณาลองใหม่อีกครั้ง</div>
                                <div className='bx-details light'><h2>Not Found</h2></div>
                            </div>
                    :
                        null
                    }
                    <div className={StartError === 2 ?'box-content-view':'box-content-view none'}>
                        <div className='bx-topic light'>
                            <p><Link to="/Subject">จัดการรายวิชา</Link> / <Link to="/Subject">รายวิชาทั้งหมด</Link> / <Link to={"/Subject/SubjectNo/"+subid}> {subjectname} </Link> / <Link to={"/Subject/SubjectNo/Exam/"+ExamNoShow}> การสอบครั้งที่ {ExamNo} </Link>/ ผลลัพธ์คะแนน</p>
                            <div className='bx-grid2-topic'>
                                <h2>แสดงผลลัพธ์คะแนน</h2>
                                
                            </div>
                        </div>
                        <div className='bx-details light'>
                            <div className="">
                                {/* <div>แสดงผลลัพธ์คะแนน</div> */}
                                <div className="bx-button" style={{ display: 'grid' }}>
                                    <div className="button-download center" onClick={handleDownload}>
                                        ดาวน์โหลดข้อมูลการสอบ
                                    </div>
                                    <div className="button-download center" onClick={handlesendemail}>
                                        <FontAwesomeIcon icon={faCircleCheck} className={sendemail !== null ? "green-font":""} /> ส่งข้อมูลการสอบไปยังอีเมลของนักศึกษา
                                    </div>
                                </div>
                                <div>
                                    <div className="bx-input-fix">
                                        <span className="flex">
                                            <input className="mgR10" style={{minWidth:25}} value="" type="checkbox" checked={showscores} onChange = {handleshowscores} />แสดงข้อมูลการสอบ
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <div>{TextError === ''? '':TextError}</div>
                            <div className="tableSub">
                                <table>
                                    <thead>
                                        <tr >
                                            {csvData.length > 0 && Object.keys(csvData[0]).map((key, index) => (
                                                <th key={index}>{key}</th>
                                            ))}
                                        </tr>
                                    </thead>
                                    <tbody>
                                            {/* Render table rows with CSV data */}
                                            {csvData.map((row, rowIndex) => (
                                                <tr key={rowIndex}>
                                                    {Object.values(row).map((value, colIndex) => (
                                                        <td key={colIndex} align="center">{value}</td>
                                                    ))}
                                                </tr>
                                            ))}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
}

export default AppScoreResults;
