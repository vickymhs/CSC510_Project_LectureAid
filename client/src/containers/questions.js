import * as React from 'react';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import BookmarkIcon from '@mui/icons-material/Bookmark';
import Button from '@mui/material/Button';
import {Accordion, AccordionSummary, AccordionDetails} from './commons';
import { makeStyles } from '@material-ui/core/styles';
import { keys } from '@mui/system';

/**
 * Defines the CSS style eleements for bookmark icons
 * @returns 
 */
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

/**
 * Renders the customised accordian for the questions fetched from the server for the page
 * @param {*} props contains the data passed on from the parent component
 * @returns {Object} HTML content for the accordians
 */
export default function CustomizedAccordions(props) {
  const [expanded, setExpanded] = React.useState("question0");
  const rows = props.results.results;
  const handleChange = (panel) => (event, newExpanded) => {
    setExpanded(newExpanded ? panel : false);
  };

  /**
   * Verfifies if a specific item has been bookmarked
   * @param {Object} item contains details about the specific item
   * @returns {boolean} true if item is bookmarked else false
   */
  const getButtonIcon = (item) => {
    let results = getBookmarksFromLocalStorage()
    if(results){
      let keys = Object.keys(results)
      return keys.includes(item.answer)
    }
    return false
  }

  /**
   * Fetches the links stored in chrome cache storage
   * @returns {Object} JSON data containing the cached information
   */
  const getBookmarksFromLocalStorage = () => {
    let linksInStorage = JSON.parse(localStorage.getItem("links"));
    return linksInStorage
  }

  /**
   * Adds a new bookmakred item to the cache storage
   * @param {Object} event points to the bookmark icon component of the selected item
   * @param {Object} item JSON data containing information about the item to be bookmarked
   */
  const addBookmarkToLocalStorage = (event, item) => {
        let link = item.answer
        let question = item.question
        let simpleAnswer = item.simple_answer
    
        let linksInStorage = JSON.parse(localStorage.getItem("links"));
        if (!linksInStorage) {
            linksInStorage = {};
        }

        let links = Object.keys(linksInStorage)
        if(links.includes(link) && question === linksInStorage[link].question && simpleAnswer === linksInStorage[link].simple_answer){
          delete linksInStorage[link]
          localStorage.setItem("links", JSON.stringify(linksInStorage));
          event.target.style.color = "grey"
        }
        else{
          linksInStorage[link] = {"question" : question, "simple_answer" : simpleAnswer}
          localStorage.setItem("links", JSON.stringify(linksInStorage));
          event.target.style.color = "dodgerblue"
        }
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
