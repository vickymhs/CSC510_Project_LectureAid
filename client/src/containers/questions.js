import * as React from 'react';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import BookmarkIcon from '@mui/icons-material/Bookmark';
import Button from '@mui/material/Button';
import {Accordion, AccordionSummary, AccordionDetails} from './commons';
import { makeStyles } from '@material-ui/core/styles';

function iconStyles() {
  return {
    bookmarkedIcon: {
      color: 'dodgerblue',
    },
    unBookmarkedIcon: {
      color: 'grey',
    },
  }
}

export default function CustomizedAccordions(props) {
  const [expanded, setExpanded] = React.useState("question0");
  const rows = props.results.results;
  const handleChange = (panel) => (event, newExpanded) => {
    setExpanded(newExpanded ? panel : false);
  };

  const getButtonIcon = (item) => {
    let results = getBookmarksFromLocalStorage()
    if(results){
      let keys = Object.keys(results)
      return keys.includes(item.answer)
    }
    return false
  }

  const getBookmarksFromLocalStorage = () => {
    let linksInStorage = JSON.parse(localStorage.getItem("links"));
    return linksInStorage
  }

  const addBookmarkToLocalStorage = (event, item) => {
        let link = item.answer
        let question = item.question
        let simpleAnswer = item.simple_answer
    
        let linksInStorage = JSON.parse(localStorage.getItem("links"));
        if (!linksInStorage) {
            linksInStorage = {};
        }
        linksInStorage[link] = {"question" : question, "simple_answer" : simpleAnswer}
        localStorage.setItem("links", JSON.stringify(linksInStorage));
        event.target.style.color = "dodgerblue"
    }
    
  const classes = makeStyles(iconStyles)();

  return (
    <div>
        {rows.map((item, index) => (
    //   <Accordion key={"question" + index} expanded={expanded === "question" + index} onChange={handleChange("question" + index)}>
    <Accordion key={"question" + index}>
        <AccordionSummary aria-controls={"question" + index + "-content"} id={"question" + index + "-header"}>
          <Typography 
            style={{
                marginRight: "auto"
            }}
          >
            {item.question}
          </Typography>
          <Button
            size="small"
            onClick={(e) => addBookmarkToLocalStorage(e,item)}>
             {getButtonIcon(item) ? <BookmarkIcon className={classes.bookmarkedIcon}/> : <BookmarkIcon className={classes.unBookmarkedIcon}/>}
          </Button>
        </AccordionSummary>
        <AccordionDetails>
            <Typography>{item.simple_answer}</Typography>
            <Link color="rgb(30,144,255)" underline="always" target="_blank" rel="noopener" href={item.answer}>
              {"Link"}
            </Link>{" "}
          </AccordionDetails>
        </Accordion>
      ))}
    </div>
  );
}
