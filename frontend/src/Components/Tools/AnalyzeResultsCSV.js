import React, { useState, useEffect } from 'react';
import Papa from 'papaparse';
import Chart from 'chart.js/auto';
import {Scatter} from "react-chartjs-2";
const AnalyzeResultsCSV = ({ url }) => {
    const [csvData, setCsvData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(url);
                const csvText = await response.text();
                Papa.parse(csvText, {
                    header: true,
                    dynamicTyping: true,
                    skipEmptyLines: true,
                    complete: function (result) {
                        console.log('Parsed CSV data:', result.data);
                        setCsvData(result.data);
                    },
                });
            } catch (error) {
                console.error('Error fetching or parsing CSV:', error);
            }
        };

        fetchData();
    }, [url]);

    
    return (
        <div>
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
            <div className='AnalyzeResultsCSV2g'>
                <div className="writing-mode">ค่าความยาก</div>
                <div>
                    <Scatter 
                        data={{
                            labels: csvData.map(obj => parseInt(obj['ข้อที่'])),
                            datasets: [
                            {
                                label: "ค่าอำนาจจำแนก,ค่าความยาก",
                                data: csvData.map(item => ({ x: item['ค่าอำนาจจำแนก'],y: item['ค่าความยาก']})),
                                backgroundColor: 'rgba(255, 99, 132, 0.6)', // Color of the dots
                                borderColor: 'rgba(255, 99, 132, 1)', // Border color of the dots
                                borderWidth: 1, // Border width of the dots
                                pointRadius: 5, // Size of the dots
                                pointHoverRadius: 8 // Size of the dots on hover
                            }
                            ]
                        }}
                        options={{
                            scales: {
                            x: {
                                type: 'linear', // X-axis type
                                position: 'bottom' // X-axis position
                            },
                            y: {
                                type: 'linear', // Y-axis type
                                position: 'left' // Y-axis position
                            }
                            }
                        }}
                            
                    />
                    <div className='center'>ค่าอำนาจจำแนก</div>
                </div>
            </div>
            
        </div>

    );
};

export default AnalyzeResultsCSV;
