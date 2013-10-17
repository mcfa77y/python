/*
 * $Id: BaseDirectoryEntryDTO.java 41186 2011-04-14 16:43:43Z jlau $
 */
package com.bricsnet.core.dal.person;

import java.io.Serializable;
import java.util.Comparator;

import org.apache.log4j.Logger;

import com.bricsnet.core.util.Constants;
import com.bricsnet.core.util.PropertyUtils;
import com.bricsnet.core.util.dto.legacy.CustomizableDTO;
import com.bricsnet.core.util.model.type.ChildBizObject;

public abstract class BaseDirectoryEntryDTO extends CustomizableDTO implements
        ChildBizObject {

    private static final Logger log = Logger
            .getLogger(BaseDirectoryEntryDTO.class);

    private static final Integer TYPE =new Integer(Constants.OBJECT_TYPE_DIRECTORY_ENTRY);

    private static String[] compareProperties = { "name", "addressOne",
            "addressTwo", "city", "country", "description", "email", "fax",
            "organization", "phone", "postalCode", "state" };

    /**
     * Compare everything except auditable fields and PK
     */
    public static final Comparator comparator = new DirComparator();

    private static final class DirComparator implements Serializable,
            Comparator {
        public int compare(Object arg0, Object arg1) {

            try {
                for (int i = 0; i < compareProperties.length; i++) {
                    if (!PropertyUtils.compareProperty(arg0,
                                                       arg1,
                                                       compareProperties[i])) {
                        String o1 = (String) PropertyUtils
                                .getProperty(arg0, compareProperties[i]);
                        String o2 = (String) PropertyUtils
                                .getProperty(arg1, compareProperties[i]);

                        return o1 != null
                            ? o1.compareTo(o2) : 1;
                    }
                }
            } catch (Exception e) {
                // required for propertyUtils. not anticipated
                log.error(e);
            }

            return 0;
        }
    }

    public abstract Integer getId();

    public abstract void setId(Integer id);

    public Integer getObjectId() {
        return getId();
    }

    public void setObjectId(Integer id) {
        setId(id);
    }

    public Integer getObjectType() {
        return TYPE;
    }

    /**
     * Fulfills contract with the BizObject
     */

    public String getAlphaId() {
        return "";
    }

}
