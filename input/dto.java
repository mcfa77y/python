/*
 * Copyright 2008 by Bricsnet FM
 *
 * This software is the confidential and proprietary information of Bricsnet FM.
 * (Confidential Information). You shall not disclose such Confidential
 * Information and shall use it only in accordance with the terms of the license
 * agreement you entered into with Bricsnet FM.
 *
 * Created on August, 2008.
 *
 * $Id: PropertyFloorDTO.java 37847 2009-07-13 18:11:50Z dpearson $
 */
package com.bricsnet.space.dal.floor;

import java.util.ArrayList;
import java.util.List;

import com.bricsnet.core.util.model.WalkTo;
import com.bricsnet.property.dal.property.PropertyDTO;
import com.bricsnet.space.dal.space.PropertySpaceDTO;

/**
 *
 * @author belal.el-ashi@cgi.com
 * @version $Revision: 37847 $
 * @since Brics|net Enterprise 5.1
 *
 */
public class PropertyFloorDTO extends BasePropertyFloorDTO {

    /** serialVersionUID property */
    private static final long serialVersionUID = -2995717007306477907L;

    private List<PropertySpaceDTO> spaces = null;

    public Integer getParentId() {
        return getPropertyId();
    }

    public void setParentId(Integer value) {
        setPropertyId(value);
    }

    public List<PropertySpaceDTO> getSpaces() {
        if (spaces == null) {
            spaces = new ArrayList<PropertySpaceDTO>();
        }
        return spaces;
    }

    public void setSpaces(List<PropertySpaceDTO> spaces) {
        this.spaces = spaces;
    }

    @Override
    public void setProperty(PropertyDTO property) {
        super.setProperty(property);
        this.setRootObject(property);
    }

    @Override
    public PropertyDTO getProperty() {
        if (property == null) {
            property = new PropertyDTO();
        }
        return property;
    }

    @Override
    public Integer getPropertyId() {
        Integer toReturn = super.getPropertyId();
        if (toReturn == null && getProperty() != null &&
                getProperty().getId() != null) {
            setPropertyId(getProperty().getId());
            toReturn = super.getPropertyId();
        }
        return toReturn;
    }

    public String getLabelKey() {
        return getAlphaId() + (getName() != null
            ? " - " + getName() : "");
    }

    private List<WalkTo> stateWalk = new ArrayList<WalkTo>();

    public void setStateWalk(List<WalkTo> stateWalk) {
        this.stateWalk = stateWalk;
    }

    public List<WalkTo> getStateWalk() {
        if (stateWalk == null) {
            stateWalk = new ArrayList<WalkTo>();
        }
        return stateWalk;
    }

}
