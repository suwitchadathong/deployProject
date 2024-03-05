
import React, {useState,useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faCloudArrowUp,faTrashCan} from "@fortawesome/free-solid-svg-icons";



function AppToolsDropZone(){
    const [csvFile, setcsvFile] = useState(''); // สำหรับเก็บไฟล์
    const [statusitem, setStatusItem] = useState(false); // สำหรับเปิด box แสดงชื่อไฟล์และลบลบไฟล์ box item
    const [namefileupload, setNameFileUpload] = useState(''); // สำหรับชื่อไฟล์อัปโหลด

    const onDrop = useCallback((acceptedFiles) => {
        console.log("OnDrop");
        console.log(acceptedFiles);
        console.log(acceptedFiles[0].type);
        if(acceptedFiles[0].type === "text/csv"){
            handleFileInputChange(acceptedFiles[0]);
        }else{
            console.log("รองรับเฉพาะไฟล์ .csv");
        }
       
    }, []);

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accepts: "image/*",
        multiple: false,
    })

    const handleFileInputChange = (e) => {
        const file = e;
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = () => {
            setcsvFile(reader.result);
        }

        setStatusItem(true);
        setNameFileUpload(file.path);

    }
    const handleSubmitFile = (e) => {
        e.preventDefault();
        if(csvFile !== ''){
            console.log("csvFile",csvFile);
        }else{
            console.log("กรุณาอัปโหลดไฟล์csvFile");
        }
    }

    const handleDelFileUpload = (e) => {
        setNameFileUpload('');
        setcsvFile('');
        setStatusItem(false);
        console.log("csvFile",csvFile);
    }

    return(
        <div>
           <div className="w300px">
                <div className="dropzone">
                    <div className="dz-box"{...getRootProps()}>
                        <input className="test" {...getInputProps()} />
                        <div className="dz-icon blue-font"><FontAwesomeIcon icon={faCloudArrowUp} /></div>
                        { isDragActive ?
                                <p>วางไฟล์ที่นี่ ...</p>:
                                <p>ลากไฟล์มาที่นี่หรืออัปโหลด</p>
                        }
                    </div>
                </div>
                {
                    statusitem?
                    <div className="box-item-name-trash space-between">
                        <div>{namefileupload}</div>
                        <div onClick={handleDelFileUpload} className="icon-Trash danger-font"><FontAwesomeIcon icon={faTrashCan} /></div>
                    </div>
                    :
                    ''
                }
                
            
                <form className="flex-end" onSubmit={handleSubmitFile}>
                    <div className='bx-button' >
                        <button type="submit"  className='button-submit'>บันทึก</button>
                    </div>
                </form >
            </div>        
        </div>
    );

}

export default AppToolsDropZone;