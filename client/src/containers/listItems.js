import * as React from "react";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import ListSubheader from "@mui/material/ListSubheader";
import AssignmentIcon from "@mui/icons-material/Assignment";
import FileUploadIcon from "@mui/icons-material/FileUpload";
import HistoryIcon from "@mui/icons-material/History";
import HomeIcon from "@mui/icons-material/Home";
import BookmarkIcon from "@mui/icons-material/Bookmark";
import ScreenSearchDesktopIcon from "@mui/icons-material/ScreenSearchDesktop";


/**
 * Contains the HTML layout the Navigation bar options for the webpage
 * @param {*} props contains the data passed on from the parent component
 * @returns HTML content for the navigational bar
 */
export const MainListItems = (props) => {
  return (
  <div>
    <ListItem button={true} onClick={() => props.clickHandler("Upload")}>
      <ListItemIcon>
        <FileUploadIcon />
      </ListItemIcon>
      <ListItemText primary="Upload" />
    </ListItem >
    <ListItem button={true} onClick={() => props.clickHandler("Home")}>
      <ListItemIcon>
        <HomeIcon />
      </ListItemIcon>
      <ListItemText primary="Home" />
    </ListItem>
    <ListItem button={true} onClick={() => props.clickHandler("Bookmarks")}>
      <ListItemIcon>
        <BookmarkIcon />
      </ListItemIcon>
      <ListItemText primary="Bookmarks" />
    </ListItem>
    <ListItem button={true} onClick={() => props.clickHandler("Online Search")}>
      <ListItemIcon>
        <ScreenSearchDesktopIcon />
      </ListItemIcon>
      <ListItemText primary="Online Search" />
    </ListItem>
    <ListItem button={true} onClick={() => props.clickHandler("History")}>
      <ListItemIcon>
        <HistoryIcon />
      </ListItemIcon>
      <ListItemText primary="History" />
    </ListItem>
  </div>

  );
}

