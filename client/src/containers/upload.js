import * as React from "react";
import axios from "axios";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import LoadingButton from "@mui/lab/LoadingButton";
import Typography from "@mui/material/Typography";

export const UploadFile = (props) => {
	const [file, setFile] = React.useState(undefined);
	const selectFile = (event) => {
		setFile(event.target.files[0]);
	};

	const [button, setButton] = React.useState("Upload");

	// React.useEffect(() => {
	// 	if (file) {
	// 		// console.log("You clicked file name" + file.name);
	// 	}
	// }, [file]);

	async function getResults(name) {
		let response = await axios.get("http://127.0.0.1:5000/get-results", { params: { filename: name.split(".")[0] } });
		// const results = await JSON.stringify(response);
		while (response.data == 404) {
			response = await axios.get("http://127.0.0.1:5000/get-results", { params: { filename: name.split(".")[0] } });
		}
		setButton("Upload");
		console.log("Results are " + JSON.stringify(response.data));
		props.getResult(response.data);

		return response;
	}

	const handleSubmission = () => {
		if (file === undefined) {
			return;
		}
		setButton("Loading");
		// Create an object of formData
		const formData = new FormData();

		// Update the formData object
		formData.append("file", file);

		// Details of the uploaded file
		console.log(file);

		// Request made to the backend api
		// Send formData object
		axios
			.post("http://127.0.0.1:5000/file-upload", formData)
			.then((response) => {
				response.data === 200 && getResults(file.name);
			})
			.catch((error) => {
				console.error("There was an error!", error);
			});
	};

	return (
		<div>
			<Typography> Upload a file!</Typography>
			<p></p>
			<Stack direction="row" alignItems="center" spacing={2}>
				<label>
					<input style={{ display: "none" }} type="file" onChange={selectFile} />
					<Button size="medium" variant="outlined" component="span" color="primary">
						Choose file
					</Button>
				</label>
				<br />
				{button === "Upload" ? (
					<Button size="medium" variant="contained" color="primary" onClick={handleSubmission}>
						Upload
					</Button>
				) : (
					<LoadingButton loading variant="outlined">
						Submit
					</LoadingButton>
				)}
			</Stack>
			{file !== undefined ? (
				<div>
					<p>Filename: {file.name}</p>
					<p>Filetype: {file.type}</p>
					<p>Size in bytes: {(file.size / 1024).toFixed(2)} KB</p>
					<p>lastModifiedDate: {file.lastModifiedDate.toLocaleDateString()}</p>
				</div>
			) : (
				<div></div>
			)}
		</div>
	);
};
