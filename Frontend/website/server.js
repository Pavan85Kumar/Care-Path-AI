const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

const uploadsDir = './uploads';
if (!fs.existsSync(uploadsDir)) {
    fs.mkdirSync(uploadsDir);
}

const storage = multer.diskStorage({
    destination: (req, file, cb) => cb(null, uploadsDir),
    filename: (req, file, cb) => cb(null, Date.now() + path.extname(file.originalname))
});

const upload = multer({
    storage: storage,
    limits: { fileSize: 5 * 1024 * 1024 }, // 5 MB limit
    fileFilter: (req, file, cb) => {
        const fileTypes = /jpeg|jpg|png|gif/;
        const extname = fileTypes.test(path.extname(file.originalname).toLowerCase());
        const mimetype = fileTypes.test(file.mimetype);
        if (extname && mimetype) return cb(null, true);
        cb(new Error('Only image files are allowed.'));
    }
});


app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.use('/assets', express.static(path.join(__dirname, 'frontend', 'assets')));
app.use('/css', express.static(path.join(__dirname, 'frontend', 'css')));
app.use('/js', express.static(path.join(__dirname, 'frontend', 'js')));


app.use('/uploads', express.static(path.join(__dirname, 'uploads')));


const pages = [
    'home', 'login', 'signup', 'dashboard', 'details',
    'doctor', 'clinics', 'plogin', 'pharma'
];

pages.forEach(page =>
    app.get(`/${page}.html`, (req, res) =>
        res.sendFile(path.join(__dirname, 'frontend', `${page}.html`))
    )
);

app.get('/', (req, res) =>
    res.sendFile(path.join(__dirname, 'frontend', 'home.html'))
);


const generateRequestId = () =>
    'REQ-' + Date.now() + '-' + Math.floor(Math.random() * 1000);


app.post('/submit', upload.single('prescription'), (req, res) => {
    const patientData = {
        requestId: generateRequestId(),
        name: req.body.name,
        age: req.body.age,
        pincode: req.body.pincode,
        gender: req.body.gender,
        pregnant: req.body.pregnant || null,
        medicines: req.body.medicines ? req.body.medicines.split(',').map(m => m.trim()) : [],
        prescription: req.file?.filename || null, // Get uploaded file name
        status: 'initiated'
    };

    fs.readFile('data.json', 'utf8', (err, data) => {
        let jsonData = [];

        if (!err && data) {
            try {
                jsonData = JSON.parse(data);
            } catch (parseErr) {
                console.error('Error parsing JSON:', parseErr);
            }
        }

        jsonData.push(patientData);

        fs.writeFile('data.json', JSON.stringify(jsonData, null, 2), 'utf8', (err) => {
            if (err) {
                console.error('Error writing file:', err);
                return res.status(500).json({ error: 'Failed to save patient data' });
            }

            res.redirect(`/details.html?message=Patient details saved successfully!&requestId=${patientData.requestId}`);
        });
    });
});


app.get('/requests', (req, res) => {
    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading data.json:', err);
            return res.status(500).json({ error: 'Error reading data file' });
        }

        try {
            const jsonData = data ? JSON.parse(data) : [];
            res.json(jsonData);
        } catch (parseErr) {
            console.error('Error parsing JSON:', parseErr);
            res.status(500).json({ error: 'Failed to parse stored data' });
        }
    });
});

app.post('/track-request', (req, res) => {
    const { request_id } = req.body;

    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) return res.status(500).json({ error: 'Error reading data file' });

        try {
            const jsonData = data ? JSON.parse(data) : [];
            const request = jsonData.find(item => item.requestId === request_id);

            if (request) {
                res.json({
                    status: 'found',
                    message: `Request ID: ${request_id} is currently in status: ${request.status}`
                });
            } else {
                res.json({
                    status: 'not found',
                    message: 'Request ID not found. Please check the ID and try again.'
                });
            }
        } catch (e) {
            res.status(500).json({ error: 'Error parsing request data' });
        }
    });
});


app.post('/process-request', (req, res) => {
    const { requestId } = req.body;

    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) return res.status(500).json({ error: 'Error reading data file' });

        try {
            const jsonData = data ? JSON.parse(data) : [];
            const request = jsonData.find(item => item.requestId === requestId);

            if (request) {
                request.status = 'processed';

                fs.writeFile('data.json', JSON.stringify(jsonData, null, 2), 'utf8', (err) => {
                    if (err) return res.status(500).json({ error: 'Error saving updated data' });
                    res.json({ status: 'success', message: `Request ${requestId} processed successfully.` });
                });
            } else {
                res.status(404).json({ status: 'error', message: 'Request not found.' });
            }
        } catch (parseErr) {
            res.status(500).json({ error: 'Failed to parse data' });
        }
    });
});


app.listen(port, () => {
    console.log(`🚀 Server running at: http://localhost:${port}`);
});
