const AWS = require('aws-sdk');
const s3 = new AWS.S3();

function generateS3Url(organizationId, fileName) {
  const params = {
    Bucket: 'your-s3-bucket-name',
    Key: `path/to/files/${organizationId}/${fileName}`,
    Expires: 60 * 5 // 5 minutes expiration time
  };

  return s3.getSignedUrl('getObject', params);
}

// Backend endpoint that generates a signed URL based on organization
app.get('/download/:organizationId/:fileName', (req, res) => {
  const { organizationId, fileName } = req.params;

  // You could also validate the organizationId here, e.g., check if it’s a valid org
  // This step can be adjusted based on your needs (e.g., no login required, just validate org ID)

  const signedUrl = generateS3Url(organizationId, fileName);
  res.json({ signedUrl });
});
